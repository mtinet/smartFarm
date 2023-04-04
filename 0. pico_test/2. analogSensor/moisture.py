# This code was written by Juhyun Kim.

from machine import ADC, Pin
import utime

# use variables instead of numbers:
soil = ADC(Pin(26)) # Connect Soil moisture sensor data to Raspberry pi pico GP26

#Calibraton values
min_moisture=0
max_moisture=65535

readDelay = 0.1 # time between readings

while True:

    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture)
    # print values
    print("moisture: " + "%.2f" % moisture +"% (adc: "+str(soil.read_u16())+")")
    utime.sleep(readDelay) # set a delay between readings
