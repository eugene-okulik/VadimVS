from test_UI_svs_pw.pages.base_page import BasePage
from test_UI_svs_pw.utils.selector_collections_eco_friendly import sort_by, sort_element, all_elements, element
from typing import Literal
import allure


class CollectionsEcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step("Сортировать по определенному параметру")
    def click_sort(self, sorting_parameter: Literal["Position", "Product Name", "Price"],
                   sort_type: Literal["asc", "desc"]):
        if sort_type == 'asc':
            self.element(sort_by).locator('nth=0').select_option(sorting_parameter)
            self.page.press(key='Enter', selector=sort_by)
        elif sort_type == 'desc':
            self.element(sort_by).locator('nth=0').select_option(sorting_parameter)
            self.page.press(key='Enter', selector=sort_by)
            self.element(sort_element).locator('nth=0').click()
        else:
            return 'Введите тип сортировки "asc" или "desc"'

    @allure.step("Проверка выполненной сортировки")
    def assert_price_after_sort(self, sort_type: Literal["asc", "desc"]):
        first = self.element(all_elements).locator('nth=0').locator(element).text_content().strip('$').split('.')[0]
        second = self.element(all_elements).locator('nth=1').locator(element).text_content().strip('$').split('.')[0]
        if sort_type == 'asc':
            assert int(first) < int(second), "do not ascending"
        elif sort_type == 'desc':
            assert int(first) > int(second), "do not descending"
        else:
            return 'Введите тип сортировки "asc" или "desc"'
