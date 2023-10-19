import json
import requests
import random
import pytest
import names
from urlfile import urlapi

def test_signup_post_API_valid():

    # Generate a random 8-digit number
    p = random.randint(10000000, 99999999)

    # Combine "01" with the random number to create the mobile number
    numb = "01" + str(p)
    header = {
        'Authorization': 'No Auth',
        "Content-Type": "application/json"
    }

    data = {
        "mobile": "01711000123",
        "otp": "5650"
    }

    response = requests.post(
        urlapi + "login-with-otp-confirm/",
        data=json.dumps(data),
        headers=header
    )


    # Check if the response status code is 200
    assert response.status_code == 200
    # Parse the response JSON data
    response_data = response.json()

    # Check the 'error' field in the response
    assert response_data["error"] is False

    # Check the 'message' field in the response
    assert response_data["message"] == "login success."

    # Check the 'status' field in the response body
    assert response_data["status"] == 200
    #
    # # Check that the 'data' field is null
    # assert response_data["data"] is None

def test_signup_post_API_invalid_numb():

    # Generate a random 8-digit number
    p = random.randint(10000000, 99999999)

    # Combine "01" with the random number to create the mobile number
    numb = "01" + str(p)
    header = {
        'Authorization': 'No Auth',
        "Content-Type": "application/json"
    }

    data = {
        "mobile": numb,
        "otp": numb
    }

    response = requests.post(
        urlapi + "login-with-otp-confirm/",
        data=json.dumps(data),
        headers=header
    )

    # Check if the response status code is 200
    assert response.status_code == 200
    # Parse the response JSON data
    response_data = response.json()

    # Check the 'error' field in the response
    assert response_data["error"] is True

    # Check the 'message' field in the response
    assert response_data["message"] == "Invalid mobile number."

    # Check the 'status' field in the response body
    assert response_data["status"] == 403

    # Check that the 'data' field is null
    assert response_data["data"] is None

def test_signup_post_API_invalid_otp():


    # Generate a random 8-digit number
    p = random.randint(10000000, 99999999)

    # Combine "01" with the random number to create the mobile number
    numb = "01" + str(p)
    header = {
        'Authorization': 'No Auth',
        "Content-Type": "application/json"
    }

    data = {
        "mobile": "01711000123",
        "otp": numb
    }

    response = requests.post(
        urlapi + "login-with-otp-confirm/",
        data=json.dumps(data),
        headers=header
    )

    # Check if the response status code is 200
    assert response.status_code == 200
    # Parse the response JSON data
    response_data = response.json()

    # Check the 'error' field in the response
    assert response_data["error"] is True

    # Check the 'message' field in the response
    assert response_data["message"] == "OTP not matched."

    # Check the 'status' field in the response body
    assert response_data["status"] == 401

    # Check that the 'data' field is null
    assert response_data["data"] is None