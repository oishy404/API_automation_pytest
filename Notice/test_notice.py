import json
import requests
import random as r
import pytest
import names
from urlfile import urlapi

nana= names.get_first_name()
def test_sport_Get_API(authentication):



    params = {
        'page': 3,
        'searchStr': '',
        'pageSize': 3
    }

    response = requests.get(urlapi + "notice-list/", headers={'Authorization': 'inherit auth from parent ' + authentication},
                            params=params)

    assert response.status_code == 200

def test_sport_Post_API(authentication):

    headers = {
        'Authorization':  authentication,
        'Content-Type': 'application/json'
    }
    data = {
        "title": nana,
        "message": nana
    }

    response = requests.post(urlapi + "create-notice/", data=json.dumps(data), headers=headers)

    assert response.status_code == 200

    # Parse the response JSON data
    response_data = response.json()
    print(response_data)
    # Check the 'error' field in the response
    # assert response_data["error"] is False
    # assert "New notice created successfully." in response_data["message"]





@pytest.fixture
def authentication():
    token = get_token()

    return token

def get_token():

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1MjNlYjYwNzU0MjdmNWUxNjFkYzJmZiIsIm5hbWUiOiJBdmkiLCJlbWFpbCI6ImF2aUBhaWRkbi5jb20iLCJtb2JpbGUiOiIwMTMxMzM0MTY3NCIsImRlcGFydG1lbnQiOiJOb3RTZXQiLCJyb2xlIjoiQWRtaW4iLCJzaWduZWRBdCI6IjIwMjMtMTAtMDlUMTI6MDA6NDEuOTQ1WiIsImlhdCI6MTY5Njg1Mjg0MSwiZXhwIjoxNjk5NDQ0ODQxfQ.RmqQCU3qWYMXmH2Wma8ch5SPGKYoQ1nxgaE1R7SQTYA"
    return token


# @pytest.fixture
# def authentication():
#     request = requests.post(urlapi +'token/',
#                                  databs)
#
#     tokens = request.json()
#
#     token = tokens["access"]
#
#
#     return token