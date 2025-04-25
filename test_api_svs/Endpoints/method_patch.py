import pytest
import requests
import allure
from test_api_svs.Endpoints.parent_method import ParentMethod
from test_api_svs.helpers.data_test import URL


class MethodPatch(ParentMethod):
    new_body = None

    @allure.step('Частичное обновление объекта')
    def partial_update(self, name, price=None, group=None):
        match (name, price, group):
            case (name, None, None):
                self.new_body = {"name": name}
            case (name, price, None):
                self.new_body = {"name": name, "data": {'price': price}}
            case (name, group, None):
                self.new_body = {"name": name, "data": {'group': group}}
            case (name, price, group):
                self.new_body = {"name": name, "data": {'group': group, 'price': price}}
            case (None, price, None):
                self.new_body = {"data": {'price': price}}
            case (None, None, group):
                self.new_body = {"data": {'group': group}}
            case (None, None, None):
                pytest.fail('Не указан параметр для изменения')
        url_with_id = f'{URL}/{self.object_id}'
        self.response = requests.patch(url=url_with_id, json=self.new_body)
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']

    @allure.step('Проверка изменения параметра "name"')
    def assert_name_for_patch(self, name):
        assert self.response_json['name'] == name, '"name" is mismatch'
