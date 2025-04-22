from test_api_svs.helpers.data_test import TEST_DATA
import pytest
import allure


@allure.title('Получение всех объектов')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('getting information')
@allure.story('get all object')
def test_meth_all_get(fixt_method_get):
    fixt_method_get.get_all_objects()
    fixt_method_get.assert_status_code()
    fixt_method_get.create_for_test()
    fixt_method_get.len_new_get()
    fixt_method_get.assert_len_with_new_obj()
    fixt_method_get.deleting_for_test()


@allure.title('Полученеи определенного объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('getting information')
@allure.story('get a specific object')
@pytest.mark.medium
def test_meth_get_by_id(fixt_method_get):
    fixt_method_get.create_for_test()
    fixt_method_get.get_object_by_id()
    fixt_method_get.assert_status_code()
    fixt_method_get.assert_key()
    fixt_method_get.assert_by_id()
    fixt_method_get.deleting_for_test()


@allure.title('Создание объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('creating an object')
@pytest.mark.critical
@pytest.mark.parametrize('name', TEST_DATA)
def test_meth_post(fixt_method_post, name):
    fixt_method_post.new_object(name)
    fixt_method_post.assert_dict_type()
    fixt_method_post.assert_srt_type()
    fixt_method_post.assert_name()
    fixt_method_post.assert_group()
    fixt_method_post.assert_price()
    fixt_method_post.deleting_for_test()


@allure.title('Полное изменение объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('full changing an object')
def test_meth_put(fixt_method_put):
    fixt_method_put.create_for_test()
    fixt_method_put.full_update()
    fixt_method_put.assert_status_code()
    fixt_method_put.assert_price()
    fixt_method_put.assert_name()
    fixt_method_put.assert_absence_param()
    fixt_method_put.deleting_for_test()


@allure.title('Частичное изменение объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('partial modification of an object')
def test_meth_patch(fixt_method_patch):
    fixt_method_patch.create_for_test()
    fixt_method_patch.partial_update()
    fixt_method_patch.assert_status_code()
    fixt_method_patch.assert_dict_type()
    fixt_method_patch.assert_name_for_patch()
    fixt_method_patch.assert_group()
    fixt_method_patch.assert_price()
    fixt_method_patch.assert_srt_type()
    fixt_method_patch.deleting_for_test()


@allure.title('Удаление объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('deleting an object')
def test_meth_delete(fixt_method_delete):
    fixt_method_delete.create_for_test()
    fixt_method_delete.deleting()
    fixt_method_delete.assert_status_code()
    fixt_method_delete.assert_delete_text()
