from test_api_svs.Endpoints.method_post import MethodPost
from test_api_svs.Endpoints.method_put import MethodPut
from test_api_svs.Endpoints.method_patch import MethodPatch
from test_api_svs.Endpoints.method_get import MethodGet
from test_api_svs.Endpoints.method_deleting import MethodDelete
import requests
import pytest


@pytest.fixture()
def fixt_method_post():
    obj = MethodPost()
    yield obj
    url_with_id = f'http://167.172.172.115:52353/object/{obj.object_id}'
    requests.delete(url=url_with_id)


@pytest.fixture()
def fixt_method_delete():
    url = 'http://167.172.172.115:52353/object'
    body = {"name": 'Тестов', "data": {'group': 1, 'price': 11}}
    object_id = requests.post(url=url, json=body).json()['id']
    obj = MethodDelete()
    obj.object_id = object_id
    return obj


@pytest.fixture()
def fixt_method_put():
    url = 'http://167.172.172.115:52353/object'
    body = {"name": 'Тестов', "data": {'group': 1, 'price': 11}}
    object_id = requests.post(url=url, json=body).json()['id']
    obj = MethodPut()
    obj.object_id = object_id
    yield obj
    url_with_id = f'http://167.172.172.115:52353/object/{object_id}'
    requests.delete(url=url_with_id)


@pytest.fixture()
def fixt_method_patch():
    url = 'http://167.172.172.115:52353/object'
    body = {"name": 'Тестов', "data": {'group': 1, 'price': 1}}
    object_id = requests.post(url=url, json=body).json()['id']
    obj = MethodPatch()
    obj.object_id = object_id
    yield obj
    url_with_id = f'http://167.172.172.115:52353/object/{object_id}'
    requests.delete(url=url_with_id)


@pytest.fixture()
def fixt_method_get():
    url = 'http://167.172.172.115:52353/object'
    body = {"name": 'Тестов', "data": {'group': 1, 'price': 11}}
    object_id = requests.post(url=url, json=body).json()['id']
    obj = MethodGet()
    obj.object_id = object_id
    yield obj
    url_with_id = f'http://167.172.172.115:52353/object/{object_id}'
    requests.delete(url=url_with_id)


@pytest.fixture()
def fixt_method_all_get():
    obj = MethodGet()
    yield obj
    url_with_id = f'http://167.172.172.115:52353/object/{obj.object_id}'
    requests.delete(url=url_with_id)
