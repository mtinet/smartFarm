# This code was written by Juhyun Kim. 

import network
import time
import urequests

# 와이파이 연결하기
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect("U+Net454C", "DDAE014478")
    print("Waiting for Wi-Fi connection", end="...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
else:
    print(wlan.ifconfig())
    print("WiFi is Connected")
    

# 시간정보 가져오기
from timezoneChange import timeOfSeoul
print(timeOfSeoul())
