from machine import Pin
import time
from dht import DHT11, InvalidChecksum
 
# Pin Clear 
for i in range(0,29):                       
    led = machine.Pin(i, machine.Pin.OUT)   
    led.value(0)
    time.sleep(0.1) # sleep 100ms
    
sensor = DHT11(Pin(15, Pin.OUT, Pin.PULL_DOWN)) #DHT11 Pin15
while True:
    temp = sensor.temperature
    humidity = sensor.humidity
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, humidity))
    time.sleep(2)
