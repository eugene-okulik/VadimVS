from test_UI_svs_pw.utils.selector_base_page import disagree_btn, title_h1
from test_UI_svs_pw.utils.selector_sale import menu_sale
from playwright.sync_api import Page, Locator, expect
import allure


class BasePage:
    url_base = "https://magento.softwaretestingboard.com/"
    response = None
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открываем страницу")
    def open_page(self):
        self.page.goto(f'{self.url_base}{self.page_url}')

    @allure.step("Открываем страницу")
    def first_page_open(self):
        self.page.goto(f'{self.url_base}{self.page_url}')
        self.close_cookie_banner()

    @allure.step("Закрыть баннер куки")
    def close_cookie_banner(self):
        self.element(disagree_btn).click()

    def element(self, selector) -> Locator:
        return self.page.locator(selector)

    @allure.step("Проверить заголовок страницы")
    def check_that_page_title_is(self, text):
        expect(self.element(title_h1)).to_have_text(text)

    @allure.step("Проверка, в каком меню сейчас находимся")
    def check_current_menu_section(self, text):
        expect(self.element(menu_sale)).to_have_text(text)
