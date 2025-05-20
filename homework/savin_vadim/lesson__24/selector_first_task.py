from selenium.webdriver.common.by import By

product_selector = (By.CSS_SELECTOR, '.card.h-100')
product_name_selector = (By.CLASS_NAME, 'name')
data_in_cart = (By.XPATH, '//tbody[@id="tbodyid"]/tr/td')
