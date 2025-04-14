import requests


def all_get():
    url = 'http://167.172.172.115:52353/object'
    get_object = requests.get(url=url)
    response = get_object.json()
    id_object = method_post()  # Чтобы убедиться что новая запись отобразится в ответе
    get_object = requests.get(url=url)
    try:
        assert get_object.status_code == 200, 'status code is incorrect'
        assert len(response['data']) + 1 == len(get_object.json()['data'])
    finally:
        method_delete(id_object)


def method_get(id_object=None):
    if id_object is None:
        id_object = method_post()
        url = f'http://167.172.172.115:52353/object/{id_object}'
        response = requests.get(url=url)
        try:
            assert response.status_code == 200, "status code is incorrect"
            assert response.json()['id'] == id_object, "'id' is incorrect"
            assert all(key in response.json() for key in ['id', 'name', 'data']), 'keys is incorrect'
        finally:
            method_delete(id_object)
    else:
        url = f'http://167.172.172.115:52353/object/{id_object}'
        response = requests.get(url=url)
        return response.json()


def method_post(name='Rulon', group=1, price=100, test_only_post=False):
    url = 'http://167.172.172.115:52353/object'
    body = {
        "name": name,
        "data":
            {
                'group': group,
                'price': price
            }
    }

    create_object = requests.post(url=url, json=body)
    response_data = create_object.json()

    if test_only_post is True:
        try:
            assert create_object.status_code == 200, "status code is incorrect"
            assert isinstance(response_data.get('data'), dict), 'data is not a dict'
            assert isinstance(response_data.get('name'), str), 'data is not a str'
            assert response_data['data']['price'] == body['data']['price'], '"price" is mismatch'
            assert response_data['data']['group'] == body['data']['group'], '"group" is mismatch'
            assert response_data['name'] == body['name'], 'name is mismatch'
        finally:
            method_delete(response_data['id'])
    else:
        return response_data['id']


def method_put(name='Test1', group=None, price=None):
    id_object = method_post("test", 1, 123)
    body = {
        "name": name,
        "data":
            {
                'price': price
            }
    }

    url = f'http://167.172.172.115:52353/object/{id_object}'
    create_object = requests.put(url=url, json=body)
    response_data = create_object.json()
    try:
        assert create_object.status_code == 200, "status code is incorrect"
        assert (response_data['data']) == {'price': None}, "'group' do not deleted"
        assert response_data.get('name') == name, "'name' is mismatch"
    finally:
        method_delete(id_object)


def method_patch(name='', group='2'):  # ToDo: переделать метод под PATCH — сейчас работает как PUT
    id_object = method_post(name="test", price=100)
    check = method_get(id_object)
    body = {
        "name": name,
        "data":
            {
                "group": group,
            }
        }

    url = f'http://167.172.172.115:52353/object/{id_object}'
    create_object = requests.put(url=url, json=body)
    response_data = create_object.json()
    try:
        assert create_object.status_code == 200, "status code is incorrect"
        assert isinstance(response_data.get('data'), dict), "'data' is not a dict"
        assert response_data['name'] == name, '"name" is mismatch'
        assert response_data['data']['price'] == check['data']['price'], "'price' is mismatch"  # ToDo
    finally:
        method_delete(id_object)


def method_delete(id_object=None):
    if id_object is None:
        id_object = method_post("test", 1, 123)

    url = f'http://167.172.172.115:52353/object/{id_object}'
    response = requests.delete(url=url)
    assert response.status_code == 200, "status code is incorrect"
    assert (response.text) == f'Object with id {id_object} successfully deleted', "text is incorrect"


all_get()  # Тестируем метод Get, получаем все данные
method_get()  # Тестируем метод GET
method_post("test", 1, 123, test_only_post=True)  # Тестируем метод Post
method_put()  # Тестируем метод Put
method_patch()  # Тестируем метод Patch
method_delete()  # Тестируем метод Delete
