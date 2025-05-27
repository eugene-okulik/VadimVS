import test_UI_svs_pw.utils.selector_create_account as locator


def locator_for_error(key):
    return getattr(locator, f'error_{key}', None)
