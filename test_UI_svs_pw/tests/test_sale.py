def test_header_h_1(sale_page):
    sale_page.first_page_open()
    sale_page.check_that_page_title_is('Sale')  # проверяем корректность заголовка h1


def test_current_menu_sale(sale_page):
    sale_page.first_page_open()
    sale_page.check_current_menu_section('Sale')  # проверяем что находимся в меню Sale


def test_redirect_to_jackets(sale_page, jackets_women_page):
    sale_page.first_page_open()
    sale_page.redirect_to_page('Pants')  # проверяем переход в другой раздел
    jackets_women_page.check_that_page_title_is('Pants')
