from test_api_svs.helpers.data_test import TEST_DATA
import pytest
import allure


@allure.title('Получение всех объектов')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('getting information')
@allure.story('get all object')
def test_meth_all_get(fixt_method_all_get):
    fixt_method_all_get.get_all_objects()
    fixt_method_all_get.assert_status_code(200)
    fixt_method_all_get.create_for_test()
    fixt_method_all_get.len_new_get()
    fixt_method_all_get.assert_len_with_new_obj()


@allure.title('Полученеи определенного объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('getting information')
@allure.story('get a specific object')
@pytest.mark.medium
def test_meth_get_by_id(fixt_method_get):
    fixt_method_get.get_object_by_id(fixt_method_get.object_id)
    fixt_method_get.assert_status_code(200)
    fixt_method_get.assert_keys('id', 'name', 'data')
    fixt_method_get.assert_by_id(fixt_method_get.object_id)


@allure.title('Создание объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('creating an object')
@pytest.mark.critical
@pytest.mark.parametrize('name', TEST_DATA)
def test_meth_post(fixt_method_post, name):
    fixt_method_post.new_object(name, group_obj=9, price_obj=99)
    fixt_method_post.assert_status_code(200)
    fixt_method_post.assert_dict_type('data')
    fixt_method_post.assert_srt_type('name')
    fixt_method_post.assert_name(name)
    fixt_method_post.assert_group(9)
    fixt_method_post.assert_price(99)


@allure.title('Полное изменение объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('full changing an object')
def test_meth_put(fixt_method_put):
    fixt_method_put.full_update(name='Код Сложнов', price=911)
    fixt_method_put.assert_status_code(200)
    fixt_method_put.assert_price(911)
    fixt_method_put.assert_name('Код Сложнов')
    fixt_method_put.assert_absence_param('group')


@allure.title('Частичное изменение объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('partial modification of an object')
def test_meth_patch(fixt_method_patch):
    fixt_method_patch.partial_update('Metod Patchev')
    fixt_method_patch.assert_status_code(200)
    fixt_method_patch.assert_dict_type('data')
    fixt_method_patch.assert_name_for_patch('Metod Patchev')
    fixt_method_patch.assert_group(1)
    fixt_method_patch.assert_price(1)
    fixt_method_patch.assert_srt_type('name')


@allure.title('Удаление объекта')
@allure.epic('testing out Evgeny Okulik API')
@allure.feature('object manipulation')
@allure.story('deleting an object')
def test_meth_delete(fixt_method_delete):
    fixt_method_delete.deleting(fixt_method_delete.object_id)
    fixt_method_delete.assert_status_code(200)
    fixt_method_delete.assert_delete_text()
