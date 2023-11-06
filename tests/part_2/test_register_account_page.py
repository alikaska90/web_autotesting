import pytest

from srv.pages.register_account_page import RegisterAccountPageElements
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/index.php?route=account/register')
    yield WebdriverObject(driver)


def test_register_account_page(webdriver_object):
    assert webdriver_object.title == 'Register Account'
    webdriver_object.wait_visible_element(RegisterAccountPageElements.LOGIN_PAGE, timeout=1)
    webdriver_object.wait_visible_element(RegisterAccountPageElements.FIRSTNAME_FIELD, timeout=1)
    webdriver_object.wait_visible_element(RegisterAccountPageElements.PASSWORD_FIELD, timeout=1)
    webdriver_object.wait_visible_element(RegisterAccountPageElements.NEWSLETTER_YES, timeout=1)
    webdriver_object.wait_visible_element(RegisterAccountPageElements.CONTINUE_BUTTON, timeout=1)
