import allure
import pytest
import requests
from test_api_svs.helpers.data_test import URL
from test_api_svs.Endpoints.parent_method import ParentMethod


class MethodDelete(ParentMethod):
    @allure.step('Удаление объекта')
    def deleting(self, id_obj):
        if id_obj:
            url_with_id = f'{URL}/{id_obj}'
            self.response = requests.delete(url=url_with_id)
        else:
            pytest.fail('Не указан ID объекта для удаления')

    @allure.step('Проверить текст об удалении определенного ID')
    def assert_delete_text(self):
        assert self.response.text == f'Object with id {self.object_id} successfully deleted', "text is incorrect"
