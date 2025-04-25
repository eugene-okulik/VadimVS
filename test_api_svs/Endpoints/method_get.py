import allure
import pytest
import requests
from test_api_svs.Endpoints.parent_method import ParentMethod
from test_api_svs.helpers.data_test import URL


class MethodGet(ParentMethod):
    len_old_get = None

    @allure.step('Получить количество объектов до создания ноовго объекта')
    def get_all_objects(self):
        self.response = requests.get(url=URL)
        self.len_old_get = len(self.response.json()['data'])
        return self.len_old_get

    @allure.step('Получение обекта по ID')
    def get_object_by_id(self, id_obj):
        if id_obj:
            url_with_id = f'{URL}/{id_obj}'
            self.response = requests.get(url=url_with_id)
            self.response_json = self.response.json()
            self.id_obj = self.response_json['id']
        else:
            pytest.fail('Не передали значение ID объекта')
        return self.id_obj

    @allure.step('Проверить что количество объектов увеличилось на 1 ')
    def assert_len_with_new_obj(self):
        self.response = requests.get(url=URL)
        len_new_get = len(self.response.json()['data'])
        assert self.len_old_get + 1 == len_new_get, 'Length of response is not equal to expected'

    @allure.step('Проверить наличие созданного объекта в БД')
    def assert_by_id(self, id_obj):
        assert id_obj == self.id_obj, 'ID is not equal to expected'

    @allure.step('Проверить наличие всех параметров у созданного объекта')
    def assert_keys(self, id_obj, name, data):
        assert all(key in self.response_json for key in [id_obj, name, data]), 'keys is incorrect'
