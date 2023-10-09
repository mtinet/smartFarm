from machine import Pin, ADC
import urequests
import time
import network
import gc
from timezoneChange import timeOfSeoul


SSID = "U+Net454C"         # 공유기의 SSID를 따옴표 안에 넣으세요.
password = "DDAE014478"       # 공유기의 password를 따옴표 안에 넣으세요.

# 와이파이 연결하기
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    # 와이파이 연결하기
    wlan.connect(SSID, password)  # 12, 13번 줄에 입력한 SSID와 password가 입력됨
    print("Waiting for Wi-Fi connection", end="...")
    print()
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
else:
    print(wlan.ifconfig())
    print("WiFi is Connected")
    print()
    
# Firebase Realtime Database 주소
url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"

# 시간정보 가져오기
updatedTime = timeOfSeoul()

# LED와 조도 센서를 연결할 핀 설정
led = Pin(1, Pin.OUT)  # 생장 LED 제어 핀
light = ADC(26)  # 조도 센서 연결 핀

while True:
    # 조도 센서에서 값 읽기
    light_value = int(light.read_u16()/16)
    
    # 시간정보 가져오기
    updatedTime = timeOfSeoul()

    # Firebase에 조도 센서 값 업데이트
    urequests.patch(url + "smartFarm.json", json={'cds': light_value, 'updatedTime': updatedTime})
    
    # 조도 센서 값이 1500보다 크면 LED 켜기, 아니면 LED 끄기
    if light_value > 1500:
        led.value(1)
    else:
        led.value(0)
    
    # 일정 시간 동안 대기 (예: 3초)
    time.sleep(3)
    gc.collect()


