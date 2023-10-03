import machine
import utime

# 조도 센서와 LED를 연결할 핀을 설정합니다.
analog_value = machine.ADC(26)
led = machine.Pin(1, machine.Pin.OUT)

while True:
    # 조도 센서에서 아날로그 값을 읽습니다.
    reading = analog_value.read_u16()/16
    print("Light Level: ", reading)
    
    # 조도가 특정 값(예: 1500)보다 높으면 LED를 켭니다.
    if reading > 1500:
        led.on()
    else:
        led.off()
    
    utime.sleep(0.2)
