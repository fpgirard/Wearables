#
# MicroPython and CircuitPython compatible code
# Supported on ESP8266
#
from machine import Pin, PWM
from time import sleep

LOW = 1
HIGH = 128

led = PWM(Pin(0))    # set GPIO0 to output to drive LED

def fade(start, stop, increment):
  for i in range(start, stop, increment):
    led.duty(i)
    sleep(20/1000)           # what happened to sleep_ms?

def main():
    while True:
        fade(LOW,HIGH,1)     # up
        fade(HIGH,LOW,-1)    # down
