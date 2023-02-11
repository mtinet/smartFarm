from machine import Pin, I2C, ADC
import network
import time
import urequests
import random
from machine import Pin
import time
from dht import DHT11, InvalidChecksum
 

# 제어할 핀 번호 설정
led = Pin(1, Pin.OUT) # 생장 LED제어 핀
fan = Pin(5, Pin.OUT) # 팬 제어
moisture = ADC(26) # 수분 감지
dht = DHT11(Pin(28, Pin.OUT, Pin.PULL_DOWN)) # 온도 감지, # 습도 감지


# 와이파이 연결하기
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    # 와이파이 연결하기, 앞에는 SSID, 뒤는 Password를 입력함 
    wlan.connect("KT_GiGA_DC1E", "027612688m")
    print("Waiting for Wi-Fi connection", end="...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
else:
    print(wlan.ifconfig())
    print("WiFi is Connected")
    print()
    

# RTDB주소
url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"


# RTDB 초기 세팅이 안되어 있는 경우 초기 세팅하기
myobjInitialize = {
    'led': 1,
    'fan': 1
    }

# myobjInitialize를 RTDB로 보내 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
urequests.patch(url+"smartFarm.json", json = myobjInitialize).json()

    
# DB 내역 가져오기
response = urequests.get(url+".json").json()
# byte형태의 데이터를 json으로 변경했기 때문에 메모리를 닫아주는 일을 하지 않아도 됨
# print(response)
# print(response['smartFarm'])
# print(response['smartFarm']['led'])


while True:
    # 현재 DB의 정보를 가져옴
    response = urequests.get(url+".json").json() # RTDB 데이터 가져오기
    moistureValue = round((1 - moisture.read_u16()/65535) * 100) # 수분센서 값 읽어오기
    temp = dht.temperature # 온도센서 값 읽어오기
    humidity = dht.humidity # 습도센서 값 읽어오기
    time.sleep(2)
    
    print("Status Check")
    print("led:", response['smartFarm']['led'], "fan:", response['smartFarm']['fan'], "Temperature: {}°C   Humidity: {:.0f}% ".format(temp, humidity), "Moisture:", moistureValue)
    print()
    
    # 현재 DB의 led 키 값의 상태에 따라 led 26번을 제어
    if (response['smartFarm']['led'] == 0) :
        led.value(0)
    else :
        led.value(1)
    
    # 현재 DB의 fan 키 값의 상태에 따라 led 27번을 제어
    if (response['smartFarm']['fan'] == 0) :
        fan.value(0)
    else :
        fan.value(1)

    # 각 객체 값 교체하기
    myobj = {
        'light': random.randrange(0, 100),
        'temp': temp,
        'humi': humidity
        }
    
    # myobj를 RTDB로 보내 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
    urequests.patch(url+"smartFarm.json", json = myobj).json()
    
    # 교체한 객체값 모니터링하기 
    print("Message Send")
    print(myobj)
    print()



