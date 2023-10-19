import json
import requests
import random
import pytest
import names
from urlfile import urlapi



def test_signup_post_API():

    # Generate a random 8-digit number
    p = random.randint(10000000, 99999999)

    # Combine "01" with the random number to create the mobile number
    numb = "01" + str(p)

    nana = names.get_first_name()

    header = {
        'Authorization': 'No Auth',
        "Content-Type": "application/json"
    }

    data = {
        "mobile": "01711000123",
        "hashCode": nana
    }

    response = requests.post(
        urlapi + "login-with-otp/",
        data=json.dumps(data),
        headers=header
    )

    assert response.status_code == 200

    # # Check if the response status code is 200
    # assert response.status_code == 403
    #
    # # Parse the response JSON data
    # response_data = response.json()
    #
    # # Check the 'error' field in the response
    # assert response_data["error"] is True
    #
    # # Check the 'message' field in the response
    # assert response_data["message"] == "invalid mobile number."
    #
    # # Check the 'status' field in the response body
    # assert response_data["status"] == 403
    #
    # # Check that the 'data' field is null
    # assert response_data["data"] is None
