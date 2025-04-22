import requests
import allure
from test_api_svs.Endpoints.parent_method import ParentMethod


class MethodPost(ParentMethod):
    @allure.step('Создание нового объекта')
    def new_object(self, name, group_obj, price_obj):
        url = 'http://167.172.172.115:52353/object'
        self.body = {"name": name, "data": {'group': group_obj, 'price': price_obj}}
        self.response = requests.post(url=url, json=self.body)
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']
