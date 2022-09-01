from machine import I2C, Pin
from ds1307 import DS1307

def get_time():
    i2c_rtc = I2C(0, scl=Pin(1), sda=Pin(0), freq = 100000)
    rtc = DS1307(i2c_rtc)

    # will return tuple that holds (year, month, date, day, hour, minute, second, p0)
    return rtc.datetime()

# now = (2022, 8, 27, 6, 14, 33, 30, 0)
# rtc.datetime(now)
# print(rtc.datetime())

def time_reset(year, month, date, day, hour, minute, second):
    rtc.datetime(year, month, date, day, hour, minute, second, 0)

if __name__ == "__main__":
    print(get_time())