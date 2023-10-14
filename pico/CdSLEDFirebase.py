from machine import Pin, ADC
import urequests
import time

# Firebase Realtime Database 주소
url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"

# LED와 조도 센서를 연결할 핀 설정
led = Pin(1, Pin.OUT)  # 생장 LED 제어 핀
light = ADC(27)  # 조도 센서 연결 핀

while True:
    # 조도 센서에서 값 읽기
    light_value = light.read_u16()
    
    # Firebase에 조도 센서 값 업데이트
    response = urequests.patch(url + "smartFarm.json", json={'cds': light_value})
    reponse.close()
    
    # 조도 센서 값이 1500보다 크면 LED 켜기, 아니면 LED 끄기
    if light_value > 1500:
        led.value(1)
    else:
        led.value(0)
    
    # 일정 시간 동안 대기 (예: 3초)
    time.sleep(3)
