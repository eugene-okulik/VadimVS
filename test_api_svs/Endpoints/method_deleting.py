import allure
import requests

from test_api_svs.Endpoints.parent_method import ParentMethod


class DeleteMethod(ParentMethod):
    @allure.step('Удаление объекта')
    def deleting(self):
        url_with_id = f'http://167.172.172.115:52353/object/{self.object_id}'
        self.response = requests.delete(url=url_with_id)

    @allure.step('Проверить текст об удалении определенного ID')
    def assert_delete_text(self):
        assert self.response.text == f'Object with id {self.object_id} successfully deleted', "text is incorrect"
