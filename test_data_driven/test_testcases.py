import requests
import json
import openpyxl
import jsonpath
from test_data_driven import test_library


def test_data_driven():
    # api
    url = "https://thetestingworldapi.com/api/studentsDetails"
    f = open("C:\\Users\\Ketaki\\Desktop\\API\\data drivn.json", 'r')
    json_req = json.loads(f.read())

    obj = test_library.common('C:/Users/Ketaki/Desktop/API/data_driven.xlsx', 'Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keylist = obj.fetch_key_names()


    for i in range(2, row+1):
        updated_json_req = obj.update_request_with_data(i, json_req, keylist)
        response = requests.post(url, updated_json_req)

        print(response.status_code)
