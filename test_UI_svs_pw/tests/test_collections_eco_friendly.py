def test_assert_header_h1(eco_friendly_page):
    eco_friendly_page.first_page_open()
    eco_friendly_page.check_that_page_title_is('Eco Friendly')  # проверяем корректность заголовка h1


def test_sort_asc(eco_friendly_page):
    eco_friendly_page.first_page_open()
    eco_friendly_page.click_sort('Price',
                                 'asc')  # проверка сортировки asc (явно бага на сайте, там она как desc указана)
    eco_friendly_page.assert_price_after_sort(sort_type='asc')


def test_sort_desc(eco_friendly_page):
    eco_friendly_page.first_page_open()
    eco_friendly_page.click_sort('Price', 'desc')  # проверка сортировки desc
    eco_friendly_page.assert_price_after_sort(sort_type='desc')
