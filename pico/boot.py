# This code was written by Juhyun Kim.

from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

led.on()
sleep(0.2)
led.off()
sleep(0.2)
led.on()
sleep(0.2)
led.off()
sleep(0.2)

import main
