import json
import requests
import random

# RTDB주소
url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"
response = requests.get(url+".json", verify=False).json()
print(response)

# 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
myobj = {'zz': '한글', 'temp': random.randrange(0, 50), 'humi': random.randrange(0,100)}
requests.patch(url+"smartFarm.json", json = myobj, verify=False).json()

