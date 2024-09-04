import requests
import json
import jsonpath
import pytest

url = "https://reqres.in/api/users"


@pytest.fixture()
def file_fixture():
    global f
    f = open("C:\\Users\\Ketaki\\Desktop\\API\\CreateUser.json", 'r')
    yield
    print("-----------------------------------------------------------")
    print("Thank you")


def test_create_new_user(file_fixture):
    json_input = f.read()
    requests_json = json.loads(json_input)
    # make post request with json input body
    response = requests.post(url, requests_json)
    print(response.content)
    print(response.headers)
    # validate response code
    assert response.status_code == 201, "status code should be 201"
    # FETCH DATA FROM RESPONSES
    json_for = json.loads(response.text)
    j_id = jsonpath.jsonpath(json_for, 'job')
    print(j_id[0])


def test_create_other_user(file_fixture):
    json_input = f.read()
    requests_json = json.loads(json_input)
    # make post request with json input body
    response = requests.post(url, requests_json)
    print(response.content)
    print(response.headers)
    # validate response code
    assert response.status_code == 201, "status code should be 201"
    # FETCH DATA FROM RESPONSES
    json_for = json.loads(response.text)
    j_id = jsonpath.jsonpath(json_for, 'job')
    print(j_id[0])
