import time
import random
from neopixel import Neopixel
import machine

# 네오픽셀의 셀 갯수, PIO 상태, 핀번호 정의
numpix = 16
PIO = 0
PixelPin = 22

# 네오픽셀이 RGB 타입일 때 네오픽셀 수, PIO 상태, 핀번호, 네오픽셀 타입 순으로 선택, 밝기 지정
strip = Neopixel(numpix, PIO, PixelPin, "RGB")

# 밝기 설정 (0~255)
strip.brightness(255)

# 아날로그 핀 설정
SoundSensorPin = machine.ADC(machine.Pin(26))

def read_sound_sensor_value(pin):
    value = pin.read_u16()
    # 여기서 범위를 수정합니다. 예를 들어, 1000에서 3000 사이로 확장할 수 있습니다.
    value = max(1500, value)  # 이 값은 센서와 환경에 따라 조정이 필요할 수 있습니다.
    value = min(2500, value)
    return value


def map_value(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low

def adjust_color_component(component):
    # 색상 성분을 랜덤하게 조정하되 최대 변경 폭은 10으로 제한
    change = random.randint(-20, 20)
    new_component = component + change
    new_component = max(0, new_component)  # 최소값은 0
    new_component = min(255, new_component)  # 최대값은 255
    return new_component

def main():
    current_color = [random.randint(0, 255) for _ in range(3)]  # 시작 색상 초기화

    try:
        last_color_change_time = time.time()

        while True:
            sound_value = read_sound_sensor_value(SoundSensorPin)
            # 여기서도 범위를 수정하여, 센서의 전체 가능한 출력 범위를 사용합니다.
            num_leds_to_light = int(map_value(sound_value, 1500, 2500, 0, numpix))

            # 매 초마다 색상 변경
            if time.time() - last_color_change_time > 1.0:
                last_color_change_time = time.time()

                # 각 색상 성분을 조정
                current_color = [adjust_color_component(c) for c in current_color]

            # LED 설정
            for i in range(numpix):
                color = tuple(current_color if i < num_leds_to_light else (0, 0, 0))
                strip.set_pixel(i, color)

            strip.show()

            # 디버깅을 위한 사운드 센서 값 출력
            print("Sound Sensor Value:", sound_value)

            # 다음 읽기까지 대기
            time.sleep(0.05)

    except KeyboardInterrupt:
        # 프로그램이 중단될 때 깨끗하게 정리합니다 (옵션).
        for i in range(numpix):
            strip.set_pixel(i, (0, 0, 0))
        strip.show()

if __name__ == "__main__":
    main()

