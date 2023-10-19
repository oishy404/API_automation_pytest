import json
import requests
import random
import pytest
import names
from urlfile import urlapi

# Global variable to store the OTP
global_random_otp = None

def test_signup_post_API():
    # Generate a random 8-digit number
    p = random.randint(10000000, 99999999)

    # Combine "01" with the random number to create the mobile number
    numb = "01" + str(p)

    nana = names.get_first_name()

    header = {
        'Authorization': 'No Auth',
        "Content-Type": "                           /json"
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

    # Check if the response status code is 200
    assert response.status_code == 200

    # Parse the response JSON data
    response_data = response.json()

    # Extract the OTP from the response data and store it in the global variable
    global global_random_otp
    global_random_otp = response_data.get("otp")

def test_signup_post_API_valid():
    # Use the OTP stored in the global variable
    otp_to_use = global_random_otp

    header = {
        'Authorization': 'No Auth',
        "Content-Type": "application/json"
    }

    data = {
        "mobile": "01711000123",
        "otp": otp_to_use
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

# # Run the tests
# if __name__ == '__main__':
#     pytest.main()
