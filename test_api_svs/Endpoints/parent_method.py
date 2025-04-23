import allure


class ParentMethod:
    object_id = None
    response = None
    response_json = None
    name = None
    body = None

    @allure.step('Проверка статус кода ')
    def assert_status_code(self, code=200):
        assert self.response.status_code == code, 'Status code is incorrect'

    @allure.step('Проверка типа данных для параметра "data"')
    def assert_dict_type(self, data):
        assert isinstance(self.response_json.get(f'{data}'), dict), '"data" is not a dict'

    @allure.step('Проверка типа данных для параметра "name"')
    def assert_srt_type(self, name):
        assert isinstance(self.response_json.get(f'{name}'), str), '"name" is not a string'

    @allure.step('Проверка параметра "price" на соотвествие')
    def assert_price(self, price):
        assert self.response_json['data']['price'] == price, '"price" is mismatch'

    @allure.step('Проверка параметра "group" на соответствие')
    def assert_group(self, group):
        assert self.response_json['data']['group'] == group, '"group" is mismatch'

    @allure.step('Проверка параметра "name" на соответствие')
    def assert_name(self, name):
        assert self.response_json['name'] == name, '"name" is mismatch'
