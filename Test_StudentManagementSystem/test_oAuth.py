import requests
import json
import jsonpath


def test_basic_oAuth():
    token_url = "https://thetestingworldapi.com/Token"
    data = {'grant_type': 'password', 'username': 'admin', 'password': ''}

    token_req = requests.post(token_url, data)
    print(token_req.text)

    token = jsonpath.jsonpath(token_req.json(), 'access_token')
    auth = {'auth': 'Bearer'+token_req[0]}
    url = "https://thetestingworldapi.com/api/StDetails/10386036"
    res = requests.get(url, headers=auth)
    print(res.text)
