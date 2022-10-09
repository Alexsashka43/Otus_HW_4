import json

import cerberus
import pytest
import requests


def test_schema(base_url, number):

    schema = {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    }

    resp = requests.get(base_url + f'/posts/{number}')
    v = cerberus.Validator()
    assert v.validate(resp.json(), schema)


def test_post_info(base_url):
    data = {
        "userId": 5,
        "title": "Some title",
        "body": "smth new"
    }

    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }

    resp = requests.post(base_url + f'/posts', data=json.dumps(data), headers=headers)
    assert resp.status_code == 201
    assert resp.json()['id'] == 101


@pytest.mark.parametrize("body", ["tgyhgfty", "ertgbfvrtyh", "324fr546ytgvf"])
@pytest.mark.parametrize("title", ["56yht", "5t454t5h", "thrth54h5"])
def test_patch_comment(base_url, number, body, title):
    data = {
        "body": body,
        "title": title
    }

    headers = {
        'Content-type': 'application/json',
        'Accept': 'text/plain'
    }

    resp = requests.patch(base_url + f'/posts/{number}', data=json.dumps(data), headers=headers)
    assert resp.json()['body'] == body and resp.json()['title'] == title


@pytest.mark.parametrize("name,username", [
    ("Leanne Graham", "Bret"),
    ("Ervin Howell", "Antonette"),
    ("Clementine Bauch", "Samantha"),
    ("Patricia Lebsack", "Karianne")
])
def test_user(base_url, name, username):
    resp = requests.get(base_url + f'/users?name={name}')
    assert resp.json()[0]['username'] == username


def test_del_posts(base_url, number):
    resp = requests.delete(base_url + f'/posts/{number}')
    assert resp.status_code == 200
    assert resp.json() == {}
