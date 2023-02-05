from machine import Pin
import time

# 빌트인 LED 모드 설정
led = Pin("LED", Pin.OUT)

# 반복동작
while True:
   led.off()
   time.sleep(1)
   led.on()
   time.sleep(1)

