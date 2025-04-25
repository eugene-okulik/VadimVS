import pytest
import requests
import allure
from test_api_svs.Endpoints.parent_method import ParentMethod
from test_api_svs.helpers.data_test import URL


class MethodPut(ParentMethod):
    @allure.step('Полное обновление обекта методом Put')
    def full_update(self, name, price=None, group=None):
        if name:
            match (price, group):
                case (None, None):
                    pytest.fail("Пропускаем тест, так как не указаны обязательные параметры.")
                case (None, group):
                    self.body = {"name": name, "data": {'group': group}}
                case (price, None):
                    self.body = {"name": name, "data": {'price': price}}
                case (price, group):
                    self.body = {"name": name, "data": {'group': group, 'price': price}}
        else:
            pytest.fail('Не указан параметр "name"')
        url_with_id = f'{URL}/{self.object_id}'
        self.response = requests.put(url=url_with_id, json=self.body)
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']

    @allure.step('Проверка на отсуствие параметра "group"')
    def assert_absence_param(self, param):
        assert f'{param}' not in self.response_json['data'], 'There should be no "param" field.'
