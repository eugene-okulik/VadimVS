from test_api_svs.Endpoints.method_deleting import DeleteMethod
from test_api_svs.Endpoints.method_post import MethodPost
from test_api_svs.Endpoints.method_put import MethodPut
from test_api_svs.Endpoints.method_patch import MethodPatch
from test_api_svs.Endpoints.method_get import MethodGet
import pytest


@pytest.fixture()
def fixt_method_post():
    return MethodPost()


@pytest.fixture()
def fixt_method_delete():
    return DeleteMethod()


@pytest.fixture()
def fixt_method_put():
    return MethodPut()


@pytest.fixture()
def fixt_method_patch():
    return MethodPatch()


@pytest.fixture()
def fixt_method_get():
    return MethodGet()
