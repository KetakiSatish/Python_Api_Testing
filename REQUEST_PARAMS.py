import requests
import json
import jsonpath

params = {'name': 'N1', 'email': 'abc@gmail.com', 'num': '1234567890'}
response = requests.get("https://httpbin.org/get", params=params)
print(response.text)
