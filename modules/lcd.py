import time
from machine import I2C, Pin
from modules.pico_i2c_lcd import I2cLcd


class LCD:
    def __init__(self, id=0, scl=1, sda=0, freq=100000):
        i2c_lcd = I2C(id=id, scl=Pin(scl), sda=Pin(sda), freq=100000)
        I2C_ADDR = i2c_lcd.scan()[0]
        self.lcd = I2cLcd(i2c_lcd, I2C_ADDR, 2, 16)

    def show_time(self, current_time, feeding_datail):
        self.lcd.move_to(0, 0)
        self.lcd.putstr(f'Time: {current_time}')
        self.lcd.move_to(0, 1)
        self.lcd.putstr(f"Feed: {feeding_datail}")


    def feeding(self, feeding_datail):
        self.lcd.move_to(0, 0)
        self.lcd.putstr('Feeding...')
        self.lcd.move_to(0, 1)
        self.lcd.putstr(f'Amount: {feeding_datail}')


    def food_amount_edit_mode(self, food_amount):
        self.lcd.backlight_on()
        self.lcd.move_to(0, 0)
        self.lcd.putstr('Edit Mode:')
        self.lcd.move_to(0, 1)
        self.lcd.putstr(f'{food_amount}')


    def clear(self):
        self.lcd.clear()


    def backlight_on(self):
        self.lcd.backlight_on()


    def backlight_off(self):
        self.lcd.backlight_off()

if __name__ == '__main__':
    LCD().show_time('12:12', '22:22/12')
    time.sleep(1)
    LCD().feeding('test')
