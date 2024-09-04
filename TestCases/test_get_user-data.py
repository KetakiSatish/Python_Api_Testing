import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users?page=2"


def test_fetching_user_details():
    # MAKING GET REQUEST
    response = requests.get(url)
    # display RESPONSE CONTENT
    print(response.content)
    print(response.headers.get('Content-Type'))
    # validate status code
    assert response.status_code == 200
    # FETCH COOKIES
    print(response.cookies)
    print(response.encoding)
    print(response.elapsed)
