import requests
import allure
from test_api_svs.Endpoints.parent_method import ParentMethod


class MethodPut(ParentMethod):
    @allure.step('Полное обновление обекта методом Put')
    def full_update(self):
        self.body = {"name": "Metod Putovich", "data": {'price': 911}}
        url_with_id = f'http://167.172.172.115:52353/object/{self.object_id}'
        self.response = requests.put(url=url_with_id, json=self.body)
        self.response_json = self.response.json()

    @allure.step('Проверка на отсуствие параметра "group"')
    def assert_absence_param(self):
        assert 'group' not in self.response_json['data'], 'There should be no "group" field.'
