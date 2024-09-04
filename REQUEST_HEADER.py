import requests
import json
import jsonpath

headerdata = {'t1': 'h1', 't2': 'h2'}
response = requests.get("https://httpbin.org/get", headers=headerdata)
print(response.text)