from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.on('dialog', lambda dialog: dialog.accept())
    page.locator('.a-button').click()
    result_locator = page.locator('#result-text')
    expect(result_locator).to_have_text('Ok')


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    locator_for_new_page = page.locator('.a-button')
    with context.expect_page() as new_page_event:
        locator_for_new_page.click()
    new_page = new_page_event.value
    expect(new_page.locator('#result-text')).to_have_text('I am a new page in a new tab')
    expect(page.locator('.a-button')).to_be_enabled()


def test_await(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_have_css(name='color', value='rgb(220, 53, 69)')
    button.click()
