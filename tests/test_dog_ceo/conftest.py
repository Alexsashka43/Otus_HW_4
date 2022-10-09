import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://dog.ceo/api",
        help="This is request url"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="Method to execute"
    )

    parser.addoption(
        "--breed",
        default=["affenpinscher", "african"],
        choices=[
            "affenpinscher", "african", "airedale", "akita", "appenzeller", "australian", "basenji",
            "beagle", "bluetick", "borzoi", "bouvier", "boxer", "brabancon", "briard", "buhund",
            "bulldog", "bullterrier", "cattledog", "chihuahua", "chow", "clumber", "cockapoo",
            "collie", "coonhound", "corgi", "cotondetulear", "dachshund", "dalmatian", "dane",
            "deerhound", "dhole", "dingo", "doberman", "elkhound", "entlebucher", "eskimo", "finnish",
            "frise", "germanshepherd", "greyhound", "groenendael", "havanese", "hound", "husky",
            "keeshond", "kelpie", "komondor", "kuvasz", "labradoodle", "labrador", "leonberg", "lhasa",
            "malamute", "malinois", "maltese", "mastiff", "mexicanhairless", "mix", "mountain",
            "newfoundland", "otterhound", "ovcharka", "papillon", "pekinese", "pembroke", "pinscher",
            "pitbull", "pointer", "pomeranian", "poodle", "pug", "puggle", "pyrenees", "redbone",
            "retriever", "ridgeback", "rottweiler", "saluki", "samoyed", "schipperke", "schnauzer",
            "setter", "sharpei", "sheepdog", "shiba", "shihtzu", "spaniel", "springer", "stbernard",
            "terrier", "tervuren", "vizsla", "waterdog", "weimaraner", "whippet", "wolfhound"
        ],
        help="Choose 2 breeds"
    )

    parser.addoption(
        "--count_images",
        default=3,
        help="Number of images"
    )




@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))


@pytest.fixture
def breed(request):
    return request.config.getoption("--breed")


@pytest.fixture
def count_images(request):
    return request.config.getoption("--count_images")
