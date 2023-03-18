import json
import requests
import random
import urllib3

# SSL인증서 경고 뜨지 않도록 세팅
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# RTDB주소
url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"
response = requests.get(url+".json", verify=False).json()
print(response)

url1 = "https://nlp-test-d817f.firebaseio.com/"
response1 = requests.get(url1+".json", verify=False).json()
print(response1)

# 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
myobj = {'ㅋㅋ': 'ㄴㄴ', 'light': random.randrange(0,100), 'temp': random.randrange(0, 50), 'humi': random.randrange(0,100)}
requests.patch(url+"smartFarm.json", json = myobj, verify=False).json()
requests.patch(url1+"smartFarm.json", json = myobj, verify=False).json()

