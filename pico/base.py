from machine import Pin, I2C
import network
import time
import urequests
import random

# 제어할 핀 번호 설정
from machine import Pin
led = Pin(26, Pin.OUT)
fan = Pin(27, Pin.OUT)


# 와이파이 연결하기
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect("KT_GiGA_DC1E", "027612688m")
    print("Waiting for Wi-Fi connection", end="...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
else:
    print(wlan.ifconfig())
    print("WiFi is Connected")

# RTDB주소
url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"

# 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
myobjInitialize = {
    'led': 0,
    'fan': 1
    }
urequests.patch(url+"smartFarm.json", json = myobjInitialize).json()
    
# DB 내역 가져오기
response = urequests.get(url+".json").json()
# byte형태의 데이터를 json으로 변경했기 때문에 메모리를 닫아주는 일을 하지 않아도 됨
# print(response)
# print(response['smartFarm'])
# print(response['smartFarm']['led'])

while True:
    # 현재 DB의 정보를 가져옴
    response = urequests.get(url+".json").json()
    print("led:", response['smartFarm']['led'], "fan:", response['smartFarm']['fan'])
    
    # 현재 DB의 led 키 값의 상태에 따라 led 26번을 제어
    if (response['smartFarm']['led'] == 0) :
        led.value(1)
    else :
        led.value(0)
    
    # 현재 DB의 fan 키 값의 상태에 따라 led 27번을 제어
    if (response['smartFarm']['fan'] == 0) :
        fan.value(1)
    else :
        fan.value(0)

    # 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
    myobj = {
        'light': random.randrange(0, 100),
        'temp': random.randrange(0, 50),
        'humi': random.randrange(0,100)
        }
    urequests.patch(url+"smartFarm.json", json = myobj).json()
    print(myobj)
    print("Message Sent.")
    print()



