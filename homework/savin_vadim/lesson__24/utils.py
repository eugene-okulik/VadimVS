from selenium.webdriver.support import expected_conditions as ec


def finding_elements(driver, search_type, selector):
    return driver.find_elements(search_type, selector)


def finding_element(driver, search_type, selector):
    return driver.find_element(search_type, selector)


def await_locator(wait, selector):
    return wait.until(ec.presence_of_element_located(selector))


def get_page(driver, url):
    driver.get(url)


def switch_tab(driver, int_tab):
    tabs = driver.window_handles
    driver.switch_to.window(tabs[int_tab])
