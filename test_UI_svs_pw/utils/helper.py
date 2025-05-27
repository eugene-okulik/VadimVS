import test_UI_svs_selenium.utils.selector_create_account as locator


def locator_for_error(key):
    return getattr(locator, f'error_{key}', None)
