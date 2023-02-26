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
print("\nQuerying the current GMT+0 time:")
time_dict = urequests.get("http://date.jsontest.com")
print(time_dict.json())
# print(time_dict.json()['date'])
# print(time_dict.json()['milliseconds_since_epoch'])
# print(time_dict.json()['time'])


def timezoneChange() :
    # UTC 기준으로 경과한 밀리초 계산
    milliseconds_since_epoch = int(time_dict.json()['milliseconds_since_epoch'])
    print(milliseconds_since_epoch)
    total_seconds = milliseconds_since_epoch // 1000
    total_minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(total_minutes, 60)

    # UTC 시간대의 날짜와 시간 계산
    date_parts = time_dict.json()["date"].split("-")
    year = int(date_parts[2])
    month = int(date_parts[0])
    day = int(date_parts[1])
    is_pm = (time_dict.json()["time"][-2:] == "PM")
    hour = int(time_dict.json()["time"][:-9])
    if is_pm and hour != 12:
        hour += 12
    minute = int(time_dict.json()["time"][-8:-6])
    second = int(time_dict.json()["time"][-5:-3])

    # GMP+9 시간대의 시간 계산
    hour += 9
    if hour >= 24:
        hour -= 24
        day += 1

    # 변환된 시간을 출력
    am_pm = "AM" if hour < 12 else "PM"
    hour = hour if hour <= 12 else hour - 12
    hour_str = str(hour) if hour >= 10 else "0" + str(hour)
    minute_str = str(minute) if minute >= 10 else "0" + str(minute)
    second_str = str(second) if second >= 10 else "0" + str(second)
    output_str = "{:02d}-{:02d}-{:04d} {}:{}:{} {}".format(month, day, year, hour_str, minute_str, second_str, am_pm)
    return(output_str)

print(timezoneChange())