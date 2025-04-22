from test_api_svs.Endpoints.method_post import MethodPost
from test_api_svs.Endpoints.method_put import MethodPut
from test_api_svs.Endpoints.method_patch import MethodPatch
from test_api_svs.Endpoints.method_get import MethodGet
from test_api_svs.Endpoints.method_deleting import MethodDelete

import pytest


@pytest.fixture()
def fixt_method_post():
    obj = MethodPost()
    yield obj
    obj.deleting_for_test()


@pytest.fixture()
def fixt_method_delete():
    obj = MethodDelete()
    obj.create_for_test()
    return obj


@pytest.fixture()
def fixt_method_put():
    obj = MethodPut()
    obj.create_for_test()
    yield obj
    obj.deleting_for_test()


@pytest.fixture()
def fixt_method_patch():
    obj = MethodPatch()
    obj.create_for_test()
    yield obj
    obj.deleting_for_test()


@pytest.fixture()
def fixt_method_get():
    obj = MethodGet()
    obj.create_for_test()
    yield obj
    obj.deleting_for_test()


@pytest.fixture()
def fixt_method_all_get():
    obj = MethodGet()
    yield obj
    obj.deleting_for_test()
