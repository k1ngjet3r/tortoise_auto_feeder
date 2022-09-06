from machine import I2C, Pin
from modules.ds1307 import DS1307


class Clock:
    def __init__(self, scl=1, sda=0):
        i2c_rtc = I2C(0, scl=Pin(scl), sda=Pin(sda), freq = 100000)
        self.rtc = DS1307(i2c_rtc)


    def get_time(self):
        # will return tuple that holds (year, month, date, day, hour, minute, second, p0)
        return self.rtc.datetime()


    def time_reset(year, month, date, day, hour, minute, second):
        self.rtc.datetime(year, month, date, day, hour, minute, second, 0)


if __name__ == "__main__":
    print(Clock.get_time())