import time
from clock import get_time
from step_motor import Stepper_motor
from lcd import lcd_show_time, lcd_feeding, lcd
from relay import Relay

def feeder(hour, minute, amount):
    while True:
        current_time = get_time()
        feeding_datail = f'{hour}:{minute}/{amount}'

        now_hour, now_minute, now_second = time_format_correction(current_time[4], current_time[5], current_time[6])

        now = f'{now_hour}:{now_minute}:{now_second}'

        # print(f'Current Time: {current_time[4]}:{current_time[5]}', end='\n')
        if current_time[4] == hour and current_time[5] == minute:
            # Turning on the relay for stepper motor
            Relay().on()
            lcd.clear()
            lcd.backlight_on()
            time.sleep(2)

            # pushing the food
            for i in range(amount):
                lcd_feeding(f'{i+1}/{amount}')
                Stepper_motor().push_food(1)
            lcd_feeding('Done!')
            time.sleep(2)
            Relay().off()
            time.sleep(60)
        else:
            lcd.backlight_off()
            lcd_show_time(now, feeding_datail)
            time.sleep(1)


def time_format_correction(hour, minute, sec):
    if len(str(hour)) == 1:
        hour = '0' + str(hour)
    if len(str(minute)) == 1:
        minute = '0' + str(minute)
    if len(str(sec)) == 1:
        sec = '0' + str(sec)

    return hour, minute, sec


if __name__ == "__main__":
    feeder(hour=21, minute=50, amount=10)
