import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

# read input json
f = open("C:\\Users\\Ketaki\\Desktop\\API\\UpdatedData.json", 'r')
json_inp = f.read()
request_json = json.loads(json_inp)

response = requests.put(url, request_json)
print(response)
print(response.content)
print(response.headers)

response_json = json.loads(response.text)

s_id = jsonpath.jsonpath(response_json, 'age')
print(s_id[0])
