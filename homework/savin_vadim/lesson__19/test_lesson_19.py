import pytest
import requests
from faker import Faker
import allure


faker = Faker('ru_RU')
faker_name = faker.name()
faker_price = faker.random_int(min=100, max=1500, step=15)
faker_group = faker.random_int(min=1, max=10, step=1)


@allure.title('Получение всех объектов')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('getting information')
@allure.story('get all object')
def test_all_get(start_end, before_after_func, response_get, method_post):
    url = 'http://167.172.172.115:52353/object'
    with allure.step('Получить все объекты, с учетом только что созданного'):
        get_object = requests.get(url=url)
    with allure.step('Проверить статус код'):
        assert get_object.status_code == 200, 'status code is incorrect'
    with allure.step('Проверка увеличение общего количества объектов на 1'):
        assert len(response_get['data']) + 1 == len(get_object.json()['data'])


@allure.title('Полученеи определенного объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('getting information')
@allure.story('get a specific object')
@pytest.mark.medium
def test_method_get(before_after_func, method_post):
    url = f"http://167.172.172.115:52353/object/{method_post['id']}"
    with allure.step('Получить созданный объект'):
        response = requests.get(url=url)
    with allure.step('Проверить статус код'):
        assert response.status_code == 200, 'status code is incorrect'
    with allure.step('Проверить, что получили, именно созданный объект'):
        assert response.json()['id'] == method_post['id'], '"id" is incorrect'
    with allure.step('Проверить наличие всех добавленных параметров'):
        assert all(key in response.json() for key in ['id', 'name', 'data']), 'keys is incorrect'


@allure.title('Создание объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('creating an object')
@pytest.mark.critical
@pytest.mark.parametrize("name", ["Рулон Обоев", "Гвоздь Молотков", "Туалет Бумагов"])
def test_method_post(before_after_func, name):
    url = 'http://167.172.172.115:52353/object'
    body = {"name": name, "data": {'group': faker_group, 'price': faker_price}}
    with allure.step('Создать объект'):
        create_object = requests.post(url=url, json=body)
    response_data = create_object.json()
    with allure.step('Проверить статус код'):
        assert create_object.status_code == 200, 'status code is incorrect'
    with allure.step('Проверить тип данных "data"'):
        assert isinstance(response_data.get('data'), dict), '"data" is not a dict'
    with allure.step('Проверить тип данных "name"'):
        assert isinstance(response_data.get('name'), str), '"name" is not a str'
    with allure.step('Проверить что "price" соответствует заданным параметрам'):
        assert response_data['data']['price'] == body['data']['price'], '"price" is mismatch'
    with allure.step('Проверить что "group" соответствует заданным параметрам'):
        assert response_data['data']['group'] == body['data']['group'], '"group" is mismatch'
    with allure.step('Проверить что "name" соответствует заданным параметрам'):
        assert response_data['name'] == body['name'], '"name" is mismatch'
    url1 = f'http://167.172.172.115:52353/object/{response_data["id"]}'
    requests.delete(url=url1)


@allure.title('Полное изменение объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('full changing an object')
def test_method_put(before_after_func, method_post):
    body = {"name": faker_name, "data": {'price': faker_price}}
    url = f'http://167.172.172.115:52353/object/{method_post["id"]}'
    with allure.step('Выполнить полное изменение объекта'):
        create_object = requests.put(url=url, json=body)
    response_data = create_object.json()
    with allure.step('Проверить статус код'):
        assert create_object.status_code == 200, 'status code is incorrect'
    with allure.step('Проверить что "price" соответствует заданным параметрам'):
        assert (response_data['data']['price']) == faker_price, '"group" do not deleted'
    with allure.step('Проверить что "name" соответствует заданным параметрам'):
        assert response_data.get('name') == faker_name, '"name" is mismatch'
    with allure.step('Проверить что параметр "group" отсутствует у объекта '):
        assert 'group' not in response_data['data'], 'There should be no (group) field.'


@allure.title('Частичное изменение объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('partial modification of an object')
def test_method_patch(before_after_func, method_post):
    body = {"name": "Гром Шумов"}
    url = f'http://167.172.172.115:52353/object/{method_post["id"]}'
    with allure.step('Выполнить частичное изменение объекта'):
        create_object = requests.patch(url=url, json=body)
    response_data = create_object.json()
    with allure.step('Проверить статус код'):
        assert create_object.status_code == 200, 'status code is incorrect'
    with allure.step('Проверить тип данных "data"'):
        assert isinstance(response_data.get('data'), dict), '"data" is not a dict'
    with allure.step('Проверить что "name" соответствует заданным параметрам'):
        assert response_data['name'] == body['name'], 'the "name" field has not been changed'
    with allure.step('Проверить что "group" соответствует заданным параметрам'):
        assert response_data['data']['group'] == method_post['data']['group'], '"group" is mismatch'
    with allure.step('Проверить что "price" соответствует заданным параметрам'):
        assert response_data['data']['price'] == method_post['data']['price'], '"price" is mismatch'


@allure.title('Удаление объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('deleting an object')
def test_method_delete(before_after_func, method_post):
    url = f'http://167.172.172.115:52353/object/{method_post["id"]}'
    with allure.step('Удалить объект'):
        response = requests.delete(url=url)
    with allure.step('Проверить статус код'):
        assert response.status_code == 200, "status code is incorrect"
    with allure.step('Проверить текст об удалении определенного ID'):
        assert response.text == f'Object with id {method_post["id"]} successfully deleted', "text is incorrect"


@pytest.fixture()
def response_get():
    url = 'http://167.172.172.115:52353/object'
    with allure.step('Получить список всех объектов'):
        response_get = requests.get(url=url).json()
    return response_get


@pytest.fixture()
def method_post():
    url = 'http://167.172.172.115:52353/object'
    body = {"name": faker_name, "data": {'group': faker_group, 'price': faker_price}}
    with allure.step('Создать объект'):
        create_object = requests.post(url=url, json=body)
    id_object = create_object.json()
    yield id_object  # пример JSON {'data': {'group': str, 'price': int}, 'id': int, 'name': str}

    url_delete = f'http://167.172.172.115:52353/object/{id_object["id"]}'
    if requests.get(url=url_delete).status_code == 200:
        with allure.step('Удалить созданный для теста объект'):
            requests.delete(url=url_delete)


@pytest.fixture(scope="session")
def start_end():
    print('\nStart testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_after_func():
    print('\nbefore test')
    yield
    print('\nafter test')
