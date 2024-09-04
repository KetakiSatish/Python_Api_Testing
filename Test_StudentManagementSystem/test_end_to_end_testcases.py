import pytest
import requests
import json
import jsonpath


def test_add_new_data():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:\\Users\\Ketaki\\Desktop\\API\\new_std.json", 'r')
    json_request = json.loads(f.read())
    response = requests.post(url, json_request)
    std_id = jsonpath.jsonpath(response.json(), 'id')
    print(std_id[0])

    tech_url = "https://thetestingworldapi.com/api/technicalskills"
    f_tech = open("C:\\Users\\Ketaki\\Desktop\\API\\tech_details.json", 'r')
    json_request_tech = json.loads(f_tech.read())
    json_request_tech['id'] = std_id[0]
    json_request_tech["st_Id"] = int(std_id[0])
    tech_resp = requests.post(tech_url, json_request_tech)
    print(tech_resp.text)

    add_url = "https://thetestingworldapi.com/api/addresses"
    f_add = open("C:\\Users\\Ketaki\\Desktop\\API\\address_detaills.json", 'r')
    json_req_address = json.loads(f_add.read())
    json_req_address["stId"] = int(std_id[0])
    address_resp = requests.post(add_url, json_req_address)
    print(address_resp)

    get_details = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(std_id[0])
    response = requests.get(get_details)
    print(response.text)

