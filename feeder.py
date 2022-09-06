import time
from machine import Pin
from modules.clock import Clock
from modules.step_motor import Stepper_motor
from modules.lcd import LCD
from modules.relay import Relay

FoodAmount = 10


# Pin Setup
clock_sda = 0
clock_scl = 1

lcd_sda = 2
lcd_scl = 3

relay_pin = 5

button_increase_pin = 14
button_decrease_pin = 15

stepper_motor_dir = 16
stepper_motor_step = 17


# Init modules
clock = Clock(scl=clock_scl, sda=clock_sda)
lcd = LCD(scl=lcd_scl, sda=lcd_sda)
relay = Relay(pin=relay_pin)
button_increase = Pin(button_increase_pin, Pin.IN, Pin.PULL_DOWN)
button_decrease = Pin(button_decrease_pin, Pin.IN, Pin.PULL_DOWN)
stepper_motor = Stepper_motor(step_pin=stepper_motor_step, dir_pin=stepper_motor_dir)


def feeder(hour, minute):
    while True:
        current_time = Clock.get_time()
        feeding_datail = f'{hour}:{minute}/{FoodAmount}'

        now_hour, now_minute, now_second = time_format_correction(current_time[4], current_time[5], current_time[6])

        now = f'{now_hour}:{now_minute}:{now_second}'

        # print(f'Current Time: {current_time[4]}:{current_time[5]}', end='\n')
        if current_time[4] == hour and current_time[5] == minute:
            # Turning on the relay for stepper motor
            Relay().on()
            LCD.clear()
            LCD.backlight_on()
            time.sleep(2)

            # pushing the food
            for i in range(FoodAmount):
                LCD.lcd_feeding(f'{i+1}/{FoodAmount}')
                Stepper_motor().push_food(1)
            LCD.lcd_feeding('Done!')
            time.sleep(2)
            Relay().off()
            time.sleep(60)
        else:
            if button_increase.value() and button_decrease.value():
                LCD.clear()
                food_amout_edit_mode()

            LCD.backlight_off()
            LCD.lcd_show_time(now, feeding_datail)
            time.sleep(1)


def food_amout_edit_mode():
    global FoodAmount
    while True:
        LCD.lcd_food_amount_edit_mode(FoodAmount)

        if button_increase.value() and button_decrease.value():
            time.sleep(3)
            if button_increase.value() and button_decrease.value():
                break
        elif button_increase.value():
            FoodAmount += 1
        elif button_decrease.value():
            FoodAmount -= 1
        

def time_format_correction(hour, minute, sec):
    if len(str(hour)) == 1:
        hour = '0' + str(hour)
    if len(str(minute)) == 1:
        minute = '0' + str(minute)
    if len(str(sec)) == 1:
        sec = '0' + str(sec)

    return hour, minute, sec


if __name__ == "__main__":
    feeder(hour=21, minute=19)
