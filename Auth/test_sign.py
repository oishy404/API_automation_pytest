import json
import requests
import random as r
import pytest
import names
from urlfile import urlapi

def generate_random_email():
    domain = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    name = ''.join(r.randint('abcdefghijklmnopqrstuvwxyz') for _ in range(8))
    email = f"{name}@{r.randint(domain)}"
    return email

def test_signup_post_API():
    headerer = {
        'Authorization': 'No Auth ',
        "Content-Type": "application/json"
    }

    # Generate random data
    name = names.get_first_name()
    email = generate_random_email()
    mobile = r.randint(10000000, 99900000)
    password = r.randint(10000, 99900)

    datam = {
        "name": name,
        "email": email,
        "mobile": mobile,
        "password": password,
        "image": "https://www.w3schools.com/w3images/avatar6.png",
        "role": "ECMember",
        "isActive": True
    }

    response = requests.post(
        urlapi + "signup/",
        data=json.dumps(datam),
        headers=headerer,
    )

    assert response.status_code == 201
