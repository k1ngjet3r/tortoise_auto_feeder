from machine import Pin
import utime


class Relay:
    def __init__(self, pin=5):
        self.relay = Pin(pin, Pin.OUT)

    def on(self):
        self.relay.value(0)

    def off(self):
        self.relay.value(1)

if __name__ == '__main__':
    Relay().off()