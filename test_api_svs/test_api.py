from test_api_svs.Endpoints.method_post import MethodPost
from test_api_svs.helpers.data_test import TEST_DATA
import pytest
import allure


@allure.title('Полное изменение объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('full changing an object')
def test_meth_put(fixt_method_put):
    fixt_method_put.full_update(name='Pukan Pogroraev', price=91)
    fixt_method_put.assert_status_code(200)
    fixt_method_put.assert_price(91)
    fixt_method_put.assert_name('Pukan Pogroraev')
    fixt_method_put.assert_absence_param('group')


@allure.title('Создание объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('creating an object')
@pytest.mark.critical
@pytest.mark.parametrize('name', TEST_DATA)
def test_meth_post(fixt_method_post, name):
    fixt_method_post.new_object(name, price=91, group=616)
    fixt_method_post.assert_status_code(200)
    fixt_method_post.assert_dict_type('data')
    fixt_method_post.assert_srt_type('name')
    fixt_method_post.assert_price(91)
    fixt_method_post.assert_group(616)
    fixt_method_post.assert_name(name)  # Передал сюда значение name так как использую параметрайз


@allure.title('Частичное изменение объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('partial modification of an object')
def test_meth_patch(fixt_method_patch):
    fixt_method_patch.partial_update(name='Kusok Oboev', price=69, group=13)
    fixt_method_patch.assert_status_code(200)
    fixt_method_patch.assert_dict_type('data')
    fixt_method_patch.assert_name('Kusok Oboev')
    fixt_method_patch.assert_price(69)


@allure.title('Удаление объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('deleting an object')
def test_meth_delete(fixt_method_delete):
    fixt_method_delete.deleting(fixt_method_delete.object_id)
    fixt_method_delete.assert_status_code(200)
    fixt_method_delete.assert_delete_text()


@allure.title('Получение всех объектов')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('getting information')
@allure.story('get all object')
def test_meth_all_get(fixt_method_all_get):
    fixt_method_all_get.get_all_objects()
    fixt_method_all_get.assert_status_code(200)
    fixt_method_all_get.object_id = MethodPost().new_object(name='Pukan Pogroraev', price=81, group=333)
    fixt_method_all_get.assert_len_with_new_obj()


@allure.title('Полученеи определенного объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('getting information')
@allure.story('get a specific object')
@pytest.mark.medium
def test_meth_get_by_id(fixt_method_get_by_id):
    fixt_method_get_by_id.get_object_by_id(fixt_method_get_by_id.object_id)
    fixt_method_get_by_id.assert_status_code(200)
    fixt_method_get_by_id.assert_by_id(fixt_method_get_by_id.object_id)
    fixt_method_get_by_id.assert_keys('id', 'name', 'data')
