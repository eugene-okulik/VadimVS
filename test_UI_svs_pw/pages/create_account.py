from playwright.sync_api import expect

from test_UI_svs_pw.pages.base_page import BasePage
from test_UI_svs_pw.utils.selector_create_account import success_message, error_message_registration, create_button, \
    input_first_name, input_last_name, input_email, input_password, input_confirm_password
import allure


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    @allure.step("Заполнение формы для создания аккаунта")
    def submit_registration_form(self, firstname=None, lastname=None, email=None, password=None, confirm_password=None):
        self.element(input_first_name).fill(firstname)
        self.element(input_last_name).fill(lastname)
        self.element(input_email).fill(email)
        self.element(input_password).fill(password)
        self.element(input_confirm_password).fill(confirm_password)
        self.click_create_account_button()

    @allure.step("Валидация фронтенд ошибки")
    def check_required_input_error(self, name_input, text):
        element = self.element(name_input)
        expect(element).to_have_text(text)

    @allure.step("Нажатие кнопки создания аккаунта")
    def click_create_account_button(self):
        self.element(create_button).click()

    @allure.step("Проверка сообщения об успешном создании аккакнта")
    def check_account_created_message(self, text):
        message = self.element(success_message)
        expect(message).to_have_text(text)

    @allure.step("Валидация ошибки, данный email уже зарегистрирован")
    def check_email_already_exists(self, text):
        message = self.element(error_message_registration)
        expect(message).to_have_text(text)
