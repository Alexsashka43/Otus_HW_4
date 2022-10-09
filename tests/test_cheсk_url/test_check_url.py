import requests


def test_check_url(base_url, status_code):
    resp = requests.get(base_url)
    assert resp.status_code == status_code
