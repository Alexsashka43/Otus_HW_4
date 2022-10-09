import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://api.openbrewerydb.org",
        help="This is request url"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="Method to execute"
    )

    parser.addoption(
        "--name_brewery",
        default="10-56 Brewing Company",
        help="Choose 2 names brewery"
    )

    parser.addoption(
        "--city",
        default="Denver",
        help="Choose city"
    )

    parser.addoption(
        "--state",
        default="New York",
        help="Choose city"
    )

    parser.addoption(
        "--count_breweries",
        default=50,
        help="Number of breweries"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))


@pytest.fixture
def name_brewery(request):
    return request.config.getoption("--name_brewery")


@pytest.fixture
def city(request):
    return request.config.getoption("--city")


@pytest.fixture
def state(request):
    return request.config.getoption("--state")


@pytest.fixture
def count_breweries(request):
    return request.config.getoption("--count_breweries")


