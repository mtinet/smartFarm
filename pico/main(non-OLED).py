from machine import Pin, I2C, ADC
import network
import time
import urequests
import random

# 제어할 핀 번호 설정
led = Pin(1, Pin.OUT) # 생장 LED제어 핀
fan = Pin(5, Pin.OUT) # 팬 제어
moisture = ADC(26) # 수분 감지
temperature = ADC(27) # 온도 감지
light = ADC(28) # 조도 감지

conversion_factor = 3.3 / 65535 # 측정값 보정 계산식 


# 이메일, 위도, 경도 표시하기(자신의 스마트팜 위치를 검색해서 넣어주세요.)
email = 'mtinet@hanmail.net'
lat = 37.4983519180861
long = 126.925286048904


# 와이파이 연결하기
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    # 와이파이 연결하기, 앞에는 SSID, 뒤는 Password를 입력함 
    # wlan.connect("KT_GiGA_DC1E", "027612688m") # 염창중 와이파이
    wlan.connect("U+Net454C", "DDAE014478") # 집 와이파이
    print("Waiting for Wi-Fi connection", end="...")
    print()
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
else:
    print(wlan.ifconfig())
    print("WiFi is Connected")
    print()
    

# RTDB주소
url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"
mapUrl = "https://smartfarmlocation-default-rtdb.firebaseio.com/"


# RTDB 초기 세팅이 안되어 있는 경우 초기 세팅하기
myobjInitialize = {
    'led': 0,
    'fan': 0
    }
# myobjInitialize를 RTDB로 보내 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
urequests.patch(url+"smartFarm.json", json = myobjInitialize).json()
print("SmartFarm has been initialized.")

# RTDB 위치 정보 초기 세팅하기
myLocation = {
    'e-mail': email,
    'lat': lat,
    'long': long
    }
# myLocation를 RTDB로 보내 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
urequests.patch(url+"location.json", json = myLocation).json()
# myLocation를 스마트팜 위치 수집용 RTDB로 보내기
urequests.patch(mapUrl+"location.json", json = myLocation).json()
print("Location Info has been sent.")
print()


# RTDB 내역 가져오기
response = urequests.get(url+".json").json()
# byte형태의 데이터를 json으로 변경했기 때문에 메모리를 닫아주는 일을 하지 않아도 됨
# print(response)
# print(response['smartFarm'])
# print(response['smartFarm']['led'])


while True:
    # 현재 DB의 정보를 가져옴
    response = urequests.get(url+".json").json() # RTDB 데이터 가져오기
    moistureValue = round((1 - moisture.read_u16()/65535) * 100) # 수분센서 값 읽어오기
    temperatureValue = round((temperature.read_u16() * conversion_factor) * 100) # 온도센서 값 읽어오기
    lightValue = round((light.read_u16()/65535) * 100) # 조도센서 값 읽어오기
    
    # 읽어온 RTDB값과 센서 값 콘솔에 출력하기
    print("Status Check")
    print("LED:", response['smartFarm']['led'], "Fan:", response['smartFarm']['fan'], "Moisture:", moistureValue, "Temperature:", temperatureValue, "Light:", lightValue )
    print()
    
    # 현재 RTDB의 led 키 값의 상태에 따라 LED 핀(1번)을 제어
    if (response['smartFarm']['led'] == 0) :
        led.value(0)
    else :
        led.value(1)
    
    # 현재 RTDB의 fan 키 값의 상태에 따라 Fan 핀(5번)을 제어
    if (response['smartFarm']['fan'] == 0) :
        fan.value(0)
    else :
        fan.value(1)

    # 실시간으로 확인된 각 객체 값을 딕셔너리에 넣기
    myobj = {
        'mois': moistureValue,
        'temp': temperatureValue,
        'light': lightValue        
        }
    
    # myobj를 RTDB로 보내 객체 값 교체하기, patch는 특정 주소의 데이터가 변경됨
    urequests.patch(url+"smartFarm.json", json = myobj).json()
    
    # 교체한 객체값 콘솔에 출력하기 
    print("Message Send")
    print(myobj)
    print()

