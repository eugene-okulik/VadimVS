from test_api_svs.Endpoints.method_patch import MethodPatch
from test_api_svs.Endpoints.method_put import MethodPut
from test_api_svs.Endpoints.method_get import MethodGet
from test_api_svs.Endpoints.method_post import MethodPost
from test_api_svs.Endpoints.method_deleting import MethodDelete
import pytest


@pytest.fixture()
def fixt_method_put():
    obj = MethodPut()
    object_id = MethodPost().new_object(name='Testov Test', price=11, group=1)
    obj.object_id = object_id
    yield obj
    MethodDelete().deleting(object_id)


@pytest.fixture()
def fixt_method_post():
    obj = MethodPost()
    yield obj
    MethodDelete().deleting(obj.object_id)


@pytest.fixture()
def fixt_method_patch():
    obj = MethodPatch()
    object_id = MethodPost().new_object(name='Testov Test', price=11, group=1)
    obj.object_id = object_id
    yield obj
    MethodDelete().deleting(obj.object_id)


@pytest.fixture()
def fixt_method_delete():
    obj = MethodDelete()
    object_id = MethodPost().new_object(name='Testov Test', price=11, group=1)
    obj.object_id = object_id
    yield obj


@pytest.fixture()
def fixt_method_all_get():
    obj = MethodGet()
    yield obj
    MethodDelete().deleting(obj.object_id)


@pytest.fixture()
def fixt_method_get_by_id():
    obj = MethodGet()
    object_id = MethodPost().new_object(name='Testov Test', price=11, group=1)
    obj.object_id = object_id
    yield obj
    MethodDelete().deleting(obj.object_id)
