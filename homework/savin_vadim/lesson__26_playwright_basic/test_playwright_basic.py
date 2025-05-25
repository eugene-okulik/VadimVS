from playwright.sync_api import Page


def test_fill_form_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='Username').fill('Username')
    page.get_by_role('textbox', name='Password').fill('SomeSecurePassword')
    page.get_by_role('button', name='Login').click()


def test_fill_automation_practice_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Rulon')
    page.get_by_placeholder('Last Name').fill('Oboev')
    page.get_by_placeholder('name@example.com').fill('name@example.com')
    page.locator('label[for="gender-radio-1"]').click()
    page.get_by_placeholder('Mobile Number').fill('8999999999')
    date_of_birth = page.locator('#dateOfBirthInput')
    date_of_birth.press('Control+a')
    date_of_birth.fill('24 May 2025')
    date_of_birth.press('Escape')
    subject = page.locator('#subjectsInput')
    subject.fill('Maths')
    subject.press(key='Tab')
    page.locator('label[for="hobbies-checkbox-1"]').click()
    page.get_by_placeholder('Current Address').fill('Test Address')
    state = page.locator('#react-select-3-input')
    state.fill('Haryana')
    state.press('Tab')
    city = page.locator('#react-select-4-input')
    city.fill('Karnal')
    city.press('Tab')
    submit_button = page.locator('button.btn-primary')
    submit_button.scroll_into_view_if_needed()
    submit_button.click()
