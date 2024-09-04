import pytest
import requests
import json
import jsonpath


def test_add_student():
    global st_id
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:\\Users\\Ketaki\\Desktop\\API\\new_std_added.json", 'r')
    json_request = json.loads(f.read())
    response = requests.post(url, json_request)
    st_id = jsonpath.jsonpath(response.json(), 'id')
    print(st_id[0])


def test_get_details():
    url = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(st_id[0])
    respons = requests.get(url)
    print(respons.text)
