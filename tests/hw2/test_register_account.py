import pytest

from srv.pages.account.account_login_page import AccountLoginPage
from srv.pages.account.created_account_page import CreatedAccountPage
from srv.pages.account.my_account_page import MyAccountPage
from srv.pages.elements.top_element import Top
from srv.pages.account.register_account_page import RegisterAccountPage
from srv.webdriver_object import WebdriverObject
from tests.hw2.test_data.new_account import CORRECT_REGISTRATION_DATA, LOGIN_DATA


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/index.php?route=account/register')
    yield WebdriverObject(driver)


def test_user_registration_positive(webdriver_object):
    register_account_page = RegisterAccountPage(webdriver_object)

    register_account_page.fill_registration_form(CORRECT_REGISTRATION_DATA) \
        .set_newsletter(True) \
        .agree_to_privacy_policy() \
        .click_continue()

    created_account_page = CreatedAccountPage(webdriver_object)
    assert webdriver_object.title == created_account_page.title

    top_my_account = Top.MyAccount(webdriver_object)
    top_my_account \
        .logout() \
        .open_login_form()

    account_login_page = AccountLoginPage(webdriver_object)
    assert webdriver_object.title == account_login_page.title

    account_login_page \
        .fill_login_form(LOGIN_DATA) \
        .click_login()

    my_account_page = MyAccountPage(webdriver_object)
    assert webdriver_object.title == my_account_page.title

    top_my_account.logout()
