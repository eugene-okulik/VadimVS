from test_UI_svs_pw.pages.base_page import BasePage
import allure


class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step("Переход в другой раздел сайта")
    def redirect_to_page(self, section):
        item_women_count = self.page.locator('//div[@class="categories-menu"]//ul').locator('nth=0').locator('li')
        count = item_women_count.count()
        for i in range(count):
            element = item_women_count.locator(f'nth={i}').text_content()
            if element.strip() == section:
                item_women_count.locator(f'nth={i}').locator('a').click()
                return
        raise AssertionError(f"Раздел с именем '{section}' не найден в меню")
