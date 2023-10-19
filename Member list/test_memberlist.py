import json
import requests
import random as r
import pytest
import names
from urlfile import urlapi


def test_sport_Get_API(authentication):

    params = {
        'page': 3,
        'searchStr': '',
        'pageSize': 3
    }

    response = requests.get(urlapi + "member-list/", headers={'Authorization': 'No Auth ' + authentication},
                            params=params)

    assert response.status_code == 200


@pytest.fixture
def authentication():
    token = get_token()

    return token

def get_token():

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzMjAxZGIwMjkzZTJlMGVhZmQ1OTNlZiIsIm5hbWUiOiJKdXdlbCIsImVtYWlsIjoiVGVzdEBnbWFpbC5jb20iLCJtb2JpbGUiOiIwMTcwMDcwNDQzNiIsImRlcGFydG1lbnQiOiJBY2NvdW50cyIsInJvbGUiOiJNZW1iZXIiLCJzaWduZWRBdCI6IjIwMjMtMTAtMDVUMDQ6NDE6NDUuODkyWiIsImlhdCI6MTY5NjQ4MDkwNSwiZXhwIjoxNjk2NTY3MzA1fQ._C_ub9oDqjTA0YmZ1bUM31gT9QiQRVA_4CN_s_U32rg"
    return token
