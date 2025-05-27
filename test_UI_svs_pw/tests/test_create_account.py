from test_UI_svs_pw.utils.selector_create_account import error_first_name
from test_UI_svs_pw.utils.test_data import text_email_already_exists, text_required_input_error, \
    text_account_created_message


def test_create_account_valid_case(register_page):  # Указать НЕ ЗАРЕГИСТРИРОВАННЫЙ email
    register_page.first_page_open()
    register_page.submit_registration_form(firstname='Ted', lastname='Testov', email='7toov@tesst.com',
                                           password='Qwerty123.', confirm_password='Qwerty123.')
    register_page.check_account_created_message(text_account_created_message)


def test_existing_email(register_page):
    register_page.first_page_open()
    register_page.submit_registration_form(firstname='Ted', lastname='Testov', email='tttesttoov@test.com',
                                           password='Qwerty123.',
                                           confirm_password='Qwerty123.')  # проверяем с зарегистрированным email
    register_page.check_email_already_exists(text_email_already_exists)


def test_empty_first_name(register_page):
    register_page.first_page_open()
    register_page.submit_registration_form(firstname='', lastname='Testov', email='test@test.com',
                                           password='Qwerty123.',
                                           confirm_password='Qwerty123.')  # проверяем с пустым именем
    register_page.check_required_input_error(error_first_name, text_required_input_error)
