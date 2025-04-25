import pytest
import requests
import allure
from test_api_svs.Endpoints.parent_method import ParentMethod
from test_api_svs.helpers.data_test import URL


class MethodPost(ParentMethod):
    @allure.step('Создание нового объекта')
    def new_object(self, name, group=None, price=None):
        if name:
            match (price, group):
                case (None, None):
                    pytest.fail('Необходимо передать group или price')
                case (None, price):
                    self.body = {"name": name, "data": {'price': price}}
                case (group, None):
                    self.body = {"name": name, "data": {'group': group}}
                case (price, group):
                    self.body = {"name": name, "data": {'group': group, 'price': price}}
        else:
            pytest.fail('Не указан параметр "name"')
        self.response = requests.post(url=URL, json=self.body)
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']
        return self.object_id
