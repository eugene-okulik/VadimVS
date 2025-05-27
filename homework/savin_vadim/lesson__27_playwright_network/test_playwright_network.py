import json

from playwright.sync_api import Page, expect, Route


def test_route_response(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'
        body = json.dumps(body)  # преобразовать снова в json
        route.fulfill(
            body=body
        )

    page.route('**/step0_iphone/digitalmat', handle_route)

    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('.rf-hcard-40').locator('nth=0').click()
    text_for_assert = page.locator('[data-autom=DigitalMat-overlay-header-0-0]')
    expect(text_for_assert).to_have_text('яблокофон 16 про')
