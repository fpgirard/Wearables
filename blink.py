#
# MicroPython and CircuitPython compatible code
# Supported on ESP8266
#
from machine import Pin
from time import sleep

def main():
    led = Pin(0, Pin.OUT)   # set GPIO0 to output to drive LED
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
