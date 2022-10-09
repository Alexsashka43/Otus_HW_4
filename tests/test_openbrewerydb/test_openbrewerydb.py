import random

import cerberus
import pytest


def test_list_breweries(base_url, request_method, count_breweries):
    resp = request_method(base_url + f'/breweries?per_page={count_breweries}')
    assert resp.status_code == 200
    assert resp.json() is not None


def test_random_brewery(base_url, request_method):
    resp_first = request_method(base_url + f'/breweries/random')
    resp_second = request_method(base_url + f'/breweries/random')
    assert resp_first.json() != resp_second.json()


def test_search_by_city(base_url, request_method, city):
    resp = request_method(base_url + f'/breweries?by_city={city}')
    assert resp.status_code == 200
    assert resp.json()[random.randint(0, len(resp.json()) - 1)]['city'] == city


@pytest.mark.parametrize("name_of_brewery",
                         ["Alphabet City Brewing Co", "Harlem Blue Beer", "Radiant Pig Craft Beers", "Death Avenue"])
def test_location_breweries(base_url, request_method, name_of_brewery, state):
    resp = request_method(base_url + f'/breweries?by_name={name_of_brewery}')
    assert resp.status_code == 200
    assert resp.json()[0]['state'] == state


@pytest.mark.parametrize("name_of_brewery",
                         ["Alphabet City Brewing Co", "Harlem Blue Beer", "Radiant Pig Craft Beers", "Death Avenue"])
def test_brewery_schema(base_url, request_method, name_of_brewery):

    schema = {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "street": {"type": "string"},
        "city": {"type": "string"},
        "state": {"type": "string"}
    }

    resp = request_method(base_url + f'/breweries?by_name={name_of_brewery}')
    v = cerberus.Validator(allow_unknown=True)
    assert v.validate(resp.json()[0], schema)
