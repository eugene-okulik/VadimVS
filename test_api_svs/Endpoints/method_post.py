import requests
import allure
from test_api_svs.Endpoints.parent_method import ParentMethod


class MethodPost(ParentMethod):
    @allure.step('Создание нового объекта')
    def new_object(self, name='Metod Postov'):
        url = 'http://167.172.172.115:52353/object'
        self.body = {"name": name, "data": {'group': 1, 'price': 150}}
        self.response = requests.post(url=url, json=self.body)
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']
