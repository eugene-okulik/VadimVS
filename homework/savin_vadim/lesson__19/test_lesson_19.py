import pytest
import requests
from faker import Faker


faker = Faker('ru_RU')
faker_name = faker.name()
faker_price = faker.random_int(min=100, max=1500, step=15)
faker_group = faker.random_int(min=1, max=10, step=1)


def test_all_get(method_all_get, method_post):
    url = 'http://167.172.172.115:52353/object'
    get_object = requests.get(url=url)
    assert get_object.status_code == 200, 'status code is incorrect'
    assert len(method_all_get['data']) + 1 == len(get_object.json()['data'])


def test_method_get(method_post):
    url = f"http://167.172.172.115:52353/object/{method_post['id']}"
    response = requests.get(url=url)
    assert response.status_code == 200, "status code is incorrect"
    assert response.json()['id'] == method_post['id'], "'id' is incorrect"
    assert all(key in response.json() for key in ['id', 'name', 'data']), 'keys is incorrect'


def test_method_post():
    url = 'http://167.172.172.115:52353/object'
    body = {"name": faker_name, "data": {'group': faker_group, 'price': faker_price}}
    create_object = requests.post(url=url, json=body)
    response_data = create_object.json()
    assert create_object.status_code == 200, "status code is incorrect"
    assert isinstance(response_data.get('data'), dict), 'data is not a dict'
    assert isinstance(response_data.get('name'), str), 'data is not a str'
    assert response_data['data']['price'] == body['data']['price'], '"price" is mismatch'
    assert response_data['data']['group'] == body['data']['group'], '"group" is mismatch'
    assert response_data['name'] == body['name'], 'name is mismatch'
    url1 = f'http://167.172.172.115:52353/object/{response_data["id"]}'
    requests.delete(url=url1)


def test_method_put(method_post):
    body = {"name": faker_name, "data": {'price': faker_price}}
    url = f'http://167.172.172.115:52353/object/{method_post["id"]}'
    create_object = requests.put(url=url, json=body)
    response_data = create_object.json()
    assert create_object.status_code == 200, "status code is incorrect"
    assert (response_data['data']['price']) == faker_price, "'group' do not deleted"
    assert response_data.get('name') == faker_name, "'name' is mismatch"
    assert 'group' not in response_data['data'], 'There should be no (group) field.'


def test_method_patch(method_post):  # рабоатет как пут и надо подумать над проверками , взять пост и гет перед началом
    body = {"name": faker_name, "data": {"group": faker_group}}
    url = f'http://167.172.172.115:52353/object/{method_post["id"]}'
    create_object = requests.put(url=url, json=body)
    response_data = create_object.json()
    assert create_object.status_code == 200, "status code is incorrect"
    assert isinstance(response_data.get('data'), dict), "'data' is not a dict"
    assert response_data['name'] == faker_name, '"name" is mismatch'
    assert response_data['data']['price'] == method_post()['data']['price'], "'price' is mismatch"  # ToDo


def test_method_delete(method_post):
    url = f'http://167.172.172.115:52353/object/{method_post["id"]}'
    response = requests.delete(url=url)
    assert response.status_code == 200, "status code is incorrect"
    assert response.text == f'Object with id {method_post["id"]} successfully deleted', "text is incorrect"


@pytest.fixture()
def method_all_get():
    url = 'http://167.172.172.115:52353/object'
    response_get = requests.get(url=url).json()
    return response_get


@pytest.fixture()
def method_post():
    url = 'http://167.172.172.115:52353/object'
    body = {"name": faker_name, "data": {'group': faker_group, 'price': faker_price}}
    create_object = requests.post(url=url, json=body)
    id_object = create_object.json()
    yield id_object  # пример JSON {'data': {'group': str, 'price': int}, 'id': int, 'name': str}
    url_delete = f'http://167.172.172.115:52353/object/{id_object["id"]}'
    requests.delete(url=url_delete)
