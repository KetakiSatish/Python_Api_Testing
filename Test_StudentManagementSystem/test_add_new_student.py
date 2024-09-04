import pytest
import requests
import json
import jsonpath


def test_add_new_student_data():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:\\Users\\Ketaki\\Desktop\\API\\add_new_student.json", 'r')
    json_request = json.loads(f.read())
    response = requests.post(url, json_request)
    print(response.text)


def test_update_student_details():
    url = "https://thetestingworldapi.com/api/studentsDetails/10386021"
    f = open("C:\\Users\\Ketaki\\Desktop\\API\\update_new_student.json", 'r')
    json_request = json.loads(f.read())
    response = requests.put(url, json_request)
    print(response.text)
    assert response.status_code == 200


def test_get_student_details():
    url = "https://thetestingworldapi.com/api/studentsDetails/10386021"
    response = requests.get(url)
    print(response.text)
    json_response = json.loads(response.text)
    print(json_response)
    # json_response = response.json()
    s_id = jsonpath.jsonpath(json_response,'data.id')
    assert s_id[0] == 10386021


def test_delete_student():
    url = "https://thetestingworldapi.com/api/studentsDetails/10386020"
    response = requests.delete(url)
    print(response.text)
    assert response.status_code == 200
