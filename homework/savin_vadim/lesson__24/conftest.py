import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


@pytest.fixture()
def action(driver):
    action = ActionChains(driver)
    yield action


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 3)
    yield wait
