from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selector_second_task import add_compare_button, compare_list, disagree_btn, product_items
from utils import switch_tab
from utils import await_locator, get_page, finding_element, finding_elements
from selector_first_task import product_selector, product_name_selector, data_in_cart


def test_added_in_cart_new_tab(driver: WebDriver, action: ActionChains, wait: WebDriverWait):
    get_page(driver, 'https://www.demoblaze.com/index.html')
    await_locator(wait, product_selector)
    elements = finding_elements(driver, *product_selector)
    action.key_down(Keys.CONTROL).click(elements[0]).key_up(Keys.CONTROL).perform()
    switch_tab(driver, 1)
    await_locator(wait, product_name_selector)
    product_name = finding_element(driver, *product_name_selector).text
    product_price = finding_element(driver, By.CLASS_NAME, 'price-container').text.split()[0].strip('$')
    finding_element(driver, By.CLASS_NAME, 'btn-success').click()
    wait.until(ec.alert_is_present())
    Alert(driver).accept()
    driver.close()
    switch_tab(driver, 0)
    get_page(driver, 'https://www.demoblaze.com/cart.html')
    await_locator(wait, data_in_cart)
    in_cart_product_name = finding_elements(driver, *data_in_cart)[1].text
    in_cart_product_price = finding_elements(driver, *data_in_cart)[2].text
    assert product_name == in_cart_product_name  # проверяем тот ли товар добавили
    assert product_price == in_cart_product_price  # проверяем что только один товар добавили


def test_move_coursor(driver: WebDriver, action: ActionChains, wait: WebDriverWait):
    get_page(driver, 'https://magento.softwaretestingboard.com/gear/bags.html')
    wait.until(ec.element_to_be_clickable(disagree_btn))
    finding_element(driver, *disagree_btn).click()
    await_locator(wait, product_items)
    elements = finding_elements(driver, *product_items)
    add_compare = finding_element(driver, *add_compare_button)
    action.move_to_element(elements[0]).move_to_element(add_compare).click().perform()
    await_locator(wait, compare_list)
    elements = finding_elements(driver, *product_items)
    added_element_for_assert = elements[0].find_element(By.XPATH, '//a[@class="product-item-link"]')
    element_from_compare = finding_element(driver, *compare_list)
    assert added_element_for_assert.text.strip() == element_from_compare.text.strip().strip('\nRemove This Item')
