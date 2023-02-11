from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum

while True:
    time.sleep(1.5)
    pin = Pin(15, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(t), "Humidity: {}".format(h))
