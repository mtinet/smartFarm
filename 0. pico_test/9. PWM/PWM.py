from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(1))

pwm.freq(100)

duty = 15000
pwm.duty_u16(duty)
