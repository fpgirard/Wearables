#
# CircuitPython code
# Supported on Gemma M0
# There is no machine API on Atmel SAMD21 port - https://circuitpython.readthedocs.io/en/3.x/docs/ 
# CircuitPython doesn't support interrupts?  WTF?
#

import digitalio, pulseio, board, adafruit_dotstar
from time import sleep
from touchio import TouchIn

dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
dot[0] = (0,0,0)

led = pulseio.PWMOut(board.D2)             # make it a PWM device

LOW = 1
HIGH = 255

def fade(start, stop, increment, delay):
  for i in range(start, stop, increment):
    led.duty_cycle = i ** 2                # 16 bit value so 255^2
    sleep(delay)

def main():
    touch2 = TouchIn(board.A2)                 # stretch goal of switching by touch
    delay = 0.02                               # let's have fun with this
    while True:
        if touch2.value:
            print("A2 touched!")
            delay = delay/2
            dot[0] = (0xFF,0x14,0x93)
        fade(LOW, HIGH, 1, delay)     # up
        fade(HIGH, LOW, -1, delay)    # down
