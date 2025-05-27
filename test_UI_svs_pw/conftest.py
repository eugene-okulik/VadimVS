import pytest
from playwright.sync_api import BrowserContext
from playwright.sync_api import Page
from test_UI_svs_pw.pages.create_account import CreateAccount
from test_UI_svs_pw.pages.collections_eco_friendly import CollectionsEcoFriendly
from test_UI_svs_pw.pages.jackets_women import JacketsWomen
from test_UI_svs_pw.pages.sale import SalePage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def register_page(page: Page):
    page = CreateAccount(page)
    yield page


@pytest.fixture()
def eco_friendly_page(page: Page):
    page = CollectionsEcoFriendly(page)
    yield page


@pytest.fixture()
def sale_page(page: Page):
    page = SalePage(page)
    yield page


@pytest.fixture()
def jackets_women_page(page: Page):
    page = JacketsWomen(page)
    yield page
