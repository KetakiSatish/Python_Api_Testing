import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

response = requests.get(url)

json_response = json.loads(response.text)

for i in range(0, 5):

    id = jsonpath.jsonpath(json_response, 'data['+str(i)+'].id')
    print(id[0])


