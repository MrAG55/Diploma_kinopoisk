

import requests


def test_api_status(base_url, api_headers):
    response = requests.get(base_url, headers=api_headers)
    assert response.status_code == 200 or response.status_code == 403
