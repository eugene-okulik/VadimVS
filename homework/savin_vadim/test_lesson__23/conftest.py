import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def options():  # с закрывающимся браузером после
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    return chrome_options


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
