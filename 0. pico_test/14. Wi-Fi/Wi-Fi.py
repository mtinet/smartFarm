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

time_dict = urequests.get("http://date.jsontest.com")
print(time_dict.json())
print(time_dict.json()['milliseconds_since_epoch'])
print(time_dict.json()['date'])
print(time_dict.json()['time'])
