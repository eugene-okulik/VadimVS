import allure
import requests
from test_api_svs.Endpoints.parent_method import ParentMethod


class MethodGet(ParentMethod):
    len_old_get = None
    new_id = None

    @allure.step('Получить количество объектов до создания ноовго объекта')
    def get_all_objects(self):
        url = 'http://167.172.172.115:52353/object'
        self.response = requests.get(url=url)
        self.len_old_get = len(self.response.json()['data'])
        return self.len_old_get

    @allure.step('Получение обекта по ID')
    def get_object_by_id(self, id_obj):
        url = f'http://167.172.172.115:52353/object/{id_obj}'
        self.response = requests.get(url=url)
        self.response_json = self.response.json()
        self.new_id = self.response_json['id']
        return self.new_id

    @allure.step('Получеие количества обектов после создание нового объекта')
    def len_new_get(self):
        url = 'http://167.172.172.115:52353/object'
        self.response = requests.get(url=url)
        self.len_new_get = len(self.response.json()['data'])
        return self.len_new_get

    @allure.step('Проверить что количество объектов увеличилось на 1 ')
    def assert_len_with_new_obj(self):
        url = 'http://167.172.172.115:52353/object'
        self.response = requests.get(url=url)
        len_new_get = len(self.response.json()['data'])
        assert self.len_old_get + 1 == len_new_get, 'Length of response is not equal to expected'

    @allure.step('Проверить наличие созданного объекта в БД')
    def assert_by_id(self, id_obj):
        assert id_obj == self.new_id, 'ID is not equal to expected'

    @allure.step('Проверить наличие всех параметров у созданного объекта')
    def assert_keys(self, id_obj, name, data):
        assert all(key in self.response.json() for key in [id_obj, name, data]), 'keys is incorrect'
