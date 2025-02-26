import time
import wiringpi as wp
import sys

def blink(_pin):
    wp.digitalWrite(_pin, 1)
    time.sleep(0.5)
    wp.digitalWrite(_pin, 0)
    time.sleep(0.5)

pin = 2
wp.wiringPiSetup()
wp.pinMode(pin, 1)

for i  in range(0, 10):
    blink(pin)