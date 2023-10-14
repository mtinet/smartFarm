from machine import Pin, ADC
import urequests
import time
import network
import gc
from timezoneChange import timeOfSeoul

SSID = "U+Net454C"
password = "DDAE014478"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect(SSID, password)
    print("Waiting for Wi-Fi connection", end="...")
    print()
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
else:
    print(wlan.ifconfig())
    print("WiFi is Connected")
    print()

url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"

updatedTime = timeOfSeoul()

led = Pin(1, Pin.OUT)
light = ADC(26)

while True:
    try:
        light_value = int(light.read_u16()/16)
        light_value = int(100-(light_value*100/4096))
        updatedTime = timeOfSeoul()

        response = urequests.patch(url + "smartFarm.json", json={'light': light_value, 'updatedTime': updatedTime})

        if light_value > 1500:
            led.value(1)
        else:
            led.value(0)

        time.sleep(3)
        gc.collect()
    except Exception as e:
        print("Error occurred:", e)
        gc.collect()
        continue

