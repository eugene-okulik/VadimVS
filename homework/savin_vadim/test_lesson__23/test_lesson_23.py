import random

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers import result_row_in_modal
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_path_one(driver):
    data = 'Abracadabra'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    driver.find_element(By.ID, 'id_text_string').send_keys(data + Keys.ENTER)
    result = driver.find_element(By.ID, 'result-text').text
    assert result == data
    print(result)


def test_path_two(driver):
    wait = WebDriverWait(driver, timeout=10)
    driver.get('https://demoqa.com/automation-practice-form')
    input_f_name = driver.find_element(By.ID, 'firstName')
    input_l_name = driver.find_element(By.ID, 'lastName')
    input_email = driver.find_element(By.ID, 'userEmail')
    radio_gender = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']")
    input_mobile = driver.find_element(By.ID, 'userNumber')
    input_birth_date = driver.find_element(By.ID, 'dateOfBirthInput')
    subject = driver.find_element(By.ID,
                                  'subjectsInput')
    checkbox_hobby = driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")
    input_current_address = driver.find_element(By.ID, 'currentAddress')
    input_state = driver.find_element(By.ID, 'react-select-3-input')
    input_city = driver.find_element(By.ID, 'react-select-4-input')
    bottom_submit = driver.find_element(By.ID, 'submit')

    input_f_name.send_keys('Testov')
    input_l_name.send_keys('Test')
    input_email.send_keys('test@test.com')
    radio_gender.click()
    input_mobile.send_keys('89000000000')
    input_birth_date.send_keys(Keys.CONTROL, 'a')
    input_birth_date.send_keys('11 Jan 2025' + Keys.ESCAPE)
    subject.send_keys('Maths')
    subject.send_keys(Keys.ENTER)
    checkbox_hobby.click()
    input_current_address.send_keys('Test')
    input_state.send_keys('Haryana' + Keys.TAB)
    input_city.send_keys('Karnal' + Keys.TAB)
    bottom_submit.click()
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'modal-title'), 'Thanks for submitting the form'))
    message_window = driver.find_element(By.CLASS_NAME, 'modal-title').text
    assert message_window == 'Thanks for submitting the form'
    print(result_row_in_modal(driver)[1:])


def test_path_3_1(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    element = driver.find_element(By.ID, 'id_choose_language')
    submit = driver.find_element(By.ID, 'submit-id-submit')
    element.click()
    select = Select(element)
    options_coutn = len(select.options)
    random_index = random.randint(1, options_coutn - 1)
    select.select_by_index(random_index)
    option_choose_text = select.first_selected_option.text
    submit.click()
    result_text = driver.find_element(By.ID, 'result-text').text
    assert option_choose_text == result_text


def test_path_3_2(driver):
    wait = WebDriverWait(driver, timeout=10)
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.XPATH, '//button[text()="Start"]').click()
    wait.until(EC.presence_of_element_located((By.ID, 'finish')))
    finish_text = driver.find_element(By.XPATH, '//div[@id="finish"]//h4').text
    assert finish_text == 'Hello World!'
