import pytest

from srv.pages.account.register_account_page import RegisterAccountPage
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/index.php?route=account/register')
    yield WebdriverObject(driver)


def test_register_account_page(webdriver_object):
    register_account_pege = RegisterAccountPage(webdriver_object)
    assert webdriver_object.title == register_account_pege.title
    register_account_pege.element(register_account_pege.LOGIN_PAGE, timeout=1)
    register_account_pege.element(register_account_pege.FIRSTNAME, timeout=1)
    register_account_pege.element(register_account_pege.PASSWORD, timeout=1)
    register_account_pege.element(register_account_pege.NEWSLETTER_YES, timeout=1)
    register_account_pege.element(register_account_pege.CONTINUE, timeout=1)
