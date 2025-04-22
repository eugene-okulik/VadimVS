import requests
import allure
from test_api_svs.Endpoints.parent_method import ParentMethod


class MethodPatch(ParentMethod):
    new_body = None

    @allure.step('Частичное обновление объекта')
    def partial_update(self):
        self.new_body = {"name": "Metod Patchev"}
        url_with_id = f'http://167.172.172.115:52353/object/{self.object_id}'
        self.response = requests.patch(url=url_with_id, json=self.new_body)
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']

    @allure.step('Проверка изменения параметра "name"')
    def assert_name_for_patch(self):
        assert self.response_json['name'] == self.new_body['name'], '"name" is mismatch'
