import json
import requests
import random
import pytest
import names
from urlfile import urlapi


def test_signup_post_API(authentication):
    p = random.randint(10000000, 99900000)
    numb = "013" + str(p)
    print("Generated Mobile Number:", numb)

    """
     This is a test case with a description.
     """
    nana = names.get_first_name()
    misaddresses = nana + "122@test.com"

    header = {
        'Authorization': authentication,
        'Content-Type': 'application/json'
    }

    data = {

        "password": "12345678",
        "confirmPassword": "12345678"
    }


    response = requests.post(
        urlapi + "profile/set/password/",
        data=json.dumps(data),
        headers=header,
    )
    assert response.status_code == 200

    # if response.status_code == 200:
    #     # Success case
    #     assert response.status_code == 200
    # else:
    #     # Handle other status codes as needed
    #     assert response.status_code == 200
    #     # Assuming success for other cases
    #     response_data = response.json()
    #     assert response_data["error"] is False
    #     assert "Profile updated successfully" in response_data["message"]

@pytest.fixture
def authentication():
    token = get_token()

    return token

def get_token():

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY1MjRkNDc2NzU0MjdmNWUxNjFkYzM0ZiIsIm5hbWUiOiJBdmkiLCJlbWFpbCI6ImF2aUBhaWRkbi5jb20iLCJtb2JpbGUiOiIwMTMxMzM0MTY3NCIsImRlcGFydG1lbnQiOiJOb3RTZXQiLCJyb2xlIjoiQWRtaW4iLCJzaWduZWRBdCI6IjIwMjMtMTAtMTBUMDQ6MzU6MDUuMzc4WiIsImlhdCI6MTY5NjkxMjUwNSwiZXhwIjoxNjk5NTA0NTA1fQ.AlP0Vl-w54jMX5U5hHduibJ-UH5J7_F05_nYGV9HxKA"
    return token
