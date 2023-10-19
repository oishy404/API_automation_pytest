import json
import requests
import random
import pytest
import names
from urlfile import urlapi

p = random.randint(1000000,9990000)
# print(p)
nana= names.get_first_name()
emailaddres = nana + "122@test.com"
random_number = random.randint(1, 100)


def test_signup_post_API():
    headerer = {'Authorization': 'No Auth ',
                "Content-Type": "application/json"}

    datam = {
        "name": "nana",
        "email": "kk@ff.com",
        "mobile": "01712233445",
        "password": "123456",
        "image": "https://www.w3schools.com/w3images/avatar6.png",
        "role": "ECMember"
    }
    response = requests.post(
        urlapi + "signup/",
        data=json.dumps(datam),
        headers=headerer,
    )

    if response.status_code == 200:
        # Success case
        assert response.status_code == 200
    else:
        # Handle other status codes as needed
        assert response.status_code == 404
        # Assuming success for other cases
        response_data = response.json()
        assert response_data["error"] is True
        assert "This email/phone is already registred." in response_data["message"]
