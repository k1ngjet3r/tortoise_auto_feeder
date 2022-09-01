import time
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

i2c_lcd = I2C(id=1, scl=Pin(3), sda=Pin(2), freq=100000)
I2C_ADDR = i2c_lcd.scan()[0]
lcd = I2cLcd(i2c_lcd, I2C_ADDR, 2, 16)

def lcd_show_time(current_time, feeding_datail):
    lcd.move_to(0, 0)
    lcd.putstr(f'Time: {current_time}')

    lcd.move_to(0, 1)
    lcd.putstr(f"Feed: {feeding_datail}")


def lcd_feeding(feeding_datail):
    lcd.move_to(0, 0)
    lcd.putstr('Feeding...')

    lcd.move_to(0, 1)
    lcd.putstr(f'Amount: {feeding_datail}')


if __name__ == '__main__':
    lcd_show_time('12:12', '22:22/12')
    time.sleep(1)
    lcd_feeding('test')
