from machine import Pin, I2C, ADC
import utime

aaa= ADC(26)
bbb = ADC(27)
ccc = ADC(28)
ddd = ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    moisture = aaa.read_u16()/16
    temp = bbb.read_u16()/16
    light = ccc.read_u16()/16
    temp11 = ddd.read_u16()/16
        
    reading = ddd.read_u16() * conversion_factor
    temperature = round(27 - (reading - 0.706) / 0.001721,2)
    print("moisture: ",moisture, "temp: ", temp, "light: ", light, "Temperature : ", temp11, temperature)
    utime.sleep(2)
