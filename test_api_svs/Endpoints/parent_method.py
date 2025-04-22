import requests
import allure


class ParentMethod:
    object_id = None
    response = None
    response_json = None
    name = None
    body = None

    @allure.step('Создание тестового объекта')
    def create_for_test(self, name='Testov Test'):
        url = 'http://167.172.172.115:52353/object'
        self.body = {"name": name, "data": {'group': 1, 'price': 150}}
        self.response = requests.post(url=url, json=self.body)
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']

    @allure.step('Удаление тестового объекта')
    def deleting_for_test(self):
        url_with_id = f'http://167.172.172.115:52353/object/{self.object_id}'
        self.response = requests.delete(url=url_with_id)

    @allure.step('Проверка статус кода ')
    def assert_status_code(self, code=200):
        assert self.response.status_code == code, 'Status code is incorrect'

    @allure.step('Проверка типа данных для параметра "data"')
    def assert_dict_type(self):
        assert isinstance(self.response_json.get('data'), dict), '"data" is not a dict'

    @allure.step('Проверка типа данных для параметра "name"')
    def assert_srt_type(self):
        assert isinstance(self.response_json.get('name'), str), '"name" is not a string'

    @allure.step('Проверка параметра "price" на соотвествие')
    def assert_price(self):
        assert self.response_json['data']['price'] == self.body['data']['price'], '"price" is mismatch'

    @allure.step('Проверка параметра "group" на соответствие')
    def assert_group(self):
        assert self.response_json['data']['group'] == self.body['data']['group'], '"group" is mismatch'

    @allure.step('Проверка параметра "name" на соответствие')
    def assert_name(self):
        assert self.response_json['name'] == self.body['name'], '"name" is mismatch'
