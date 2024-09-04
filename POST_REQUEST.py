import requests
import json
import jsonpath

url = "https://reqres.in/api/users"

# read input json
f = open("C:\\Users\\Ketaki\\Desktop\\API\\CreateUser.json", 'r')
json_input = f.read()

requests_json = json.loads(json_input)
print(requests_json)

response = requests.post(url, requests_json)
print(response.content)
print(response.headers)

assert response.status_code == 201

# FETCH DATA FROM RESPONSES
json_for = json.loads(response.text)
j_id = jsonpath.jsonpath(json_for, 'job')
print(j_id[0])


