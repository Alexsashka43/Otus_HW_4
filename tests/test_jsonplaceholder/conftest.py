import pytest



def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://jsonplaceholder.typicode.com",
        help="This is request url"
    )

    parser.addoption(
        "--number",
        default=1,
        help="Choose city"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def number(request):
    return request.config.getoption("--number")
