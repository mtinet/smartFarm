import time
import machine
from machine import Pin
import _thread

# LED 핀 설정
led1 = Pin(1, Pin.OUT)
led2 = Pin(5, Pin.OUT)

# 첫 번째 LED 깜빡이기 (메인 코어에서 실행됨)
def blink_led1():
    while True:
        led1.toggle()
        time.sleep(0.5)

# 두 번째 LED 깜빡이기 (다른 코어에서 실행됨)
def blink_led2():
    while True:
        led2.toggle()
        time.sleep(1.5)

# 다른 코어에서 blink_led2 함수 실행
_thread.start_new_thread(blink_led2, ())

# 메인 코어에서 blink_led1 함수 실행
blink_led1()
