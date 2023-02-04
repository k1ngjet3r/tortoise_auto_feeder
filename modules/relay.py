from machine import Pin
import time


class Relay:
    def __init__(self, pin=13):
        self.relay = Pin(pin, Pin.OUT)

    def on(self):
        self.relay.value(0)

    def off(self):
        self.relay.value(1)

if __name__ == '__main__':
    Relay().on()
    