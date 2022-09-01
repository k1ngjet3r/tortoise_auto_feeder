from machine import Pin
import time
from time import sleep_ms
from time import sleep_us


def map(x, in_min, in_max, out_min, out_max): 
    return int((x - in_min) * (out_max - out_min) /
               (in_max - in_min) + out_min)
    
class Stepper_motor:
    def __init__(self, step_pin=17, dir_pin=16):
        self._step = Pin(step_pin, Pin.OUT)
        self._dir = Pin(dir_pin, Pin.OUT)

    def _rotate(self, angle=0, rotation='cw'):
        num_of_steps = map(angle, 0, 360, 0, 200)
        
        self._dir.value(0)
        for i in range(0,num_of_steps,1):
            self._step.value(1)
            time.sleep(0.05)
            self._step.value(0)
            time.sleep(0.05)
            
    def push_food(self, amount, speed=1):
        for i in range(amount):
            self._rotate(angle=45)
            time.sleep(speed)


if __name__ == '__main__':
    stepper = Stepper_motor(step_pin=17, dir_pin=16)

    stepper.push_food(amount=8, speed=0.1)