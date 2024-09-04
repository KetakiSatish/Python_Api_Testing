import requests
from requests.auth import HTTPBasicAuth


def test_basic():
    response = requests.get("https://github.com/users", auth=HTTPBasicAuth('ketkinsatish@gmail.com', 'Ketish@07'))
    print(response.text)
