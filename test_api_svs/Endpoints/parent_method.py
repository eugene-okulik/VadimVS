import requests
import allure


class ParentMethod:
    object_id = None
    response = None
    response_json = None
    name = None
    body = None

    def create_for_test(self, name='Testov Test', group_data=1, price_data=1):
        url = 'http://167.172.172.115:52353/object'
        self.body = {"name": name, "data": {'group': group_data, 'price': price_data}}
        self.response = requests.post(url=url, json=self.body)
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']

    def deleting_for_test(self):
        url_with_id = f'http://167.172.172.115:52353/object/{self.object_id}'
        self.response = requests.delete(url=url_with_id)

    @allure.step('Проверка статус кода ')
    def assert_status_code(self, code=200):
        assert self.response.status_code == code, 'Status code is incorrect'

    @allure.step('Проверка типа данных для параметра "data"')
    def assert_dict_type(self, data):
        assert isinstance(self.response_json.get(f'{data}'), dict), '"data" is not a dict'

    @allure.step('Проверка типа данных для параметра "name"')
    def assert_srt_type(self, name):
        assert isinstance(self.response_json.get(f'{name}'), str), '"name" is not a string'

    # пример JSON {'data': {'group': str, 'price': int}, 'id': int, 'name': str}
    @allure.step('Проверка параметра "price" на соотвествие')
    def assert_price(self, price):
        assert self.response_json['data']['price'] == price, '"price" is mismatch'

    @allure.step('Проверка параметра "group" на соответствие')
    def assert_group(self, group):
        assert self.response_json['data']['group'] == group, '"group" is mismatch'

    @allure.step('Проверка параметра "name" на соответствие')
    def assert_name(self, name):
        assert self.response_json['name'] == name, '"name" is mismatch'
