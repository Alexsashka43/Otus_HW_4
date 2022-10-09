import pytest


def test_all_dogs(base_url, request_method):
    resp = request_method(base_url + f'/breeds/list/all')
    assert resp.status_code == 200
    assert resp.json()['message'] is not None


def test_dog_random(base_url, request_method, count_images):
    resp = request_method(base_url + f'/breeds/image/random/{count_images}')
    assert resp.status_code == 200
    assert resp.json()['status'] == 'success'
    assert len(resp.json()['message']) == count_images #количество элементов в ответе соответсвует запрашиваемому количеству


@pytest.mark.parametrize("breed1,breed2", [
            ("maltese", "mastiff"),
            ("mexicanhairless", "mix"),
            ("mountain", "newfoundland"),
            ("otterhound", "ovcharka"),
            ("papillon", "pekinese"),
            ("pembroke", "pinscher"),
            ("pitbull", "pointer")
])
def test_breed(base_url, request_method, breed1, breed2):
    resp_first = request_method(base_url + f'/breed/{breed1}/images')
    resp_second = request_method(base_url + f'/breed/{breed2}/images')
    assert resp_first.status_code == 200
    assert resp_second.status_code == 200
    assert resp_first.json()['message'] != resp_second.json()['message']


@pytest.mark.parametrize("param", ["chow", "clumber", "cockapoo", "collie", "coonhound", "corgi"])
def test_sub_breed(base_url, request_method, param):
    resp = request_method(base_url + f'/breed/{param}/images')
    assert resp.status_code == 200
    assert resp.json()['status'] == 'success'


def test_breeds_list(base_url, request_method, breed):
    resp = request_method(base_url + f'/breed/{breed[0]}/images/random')
    assert resp.status_code == 200
    assert resp.json()['message'].find('.jpg')
