import pytest

from srv.pages.admin.login_admin_page import LoginAdminPage
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/admin')
    yield WebdriverObject(driver)


def test_login_admin_page(webdriver_object):
    login_admin_page = LoginAdminPage(webdriver_object)
    assert webdriver_object.title == login_admin_page.title
    login_admin_page.element(login_admin_page.USERNAME, timeout=1)
    login_admin_page.element(login_admin_page.PASSWORD, timeout=1)
    login_admin_page.element(login_admin_page.LOGIN_BUTTON, timeout=1)
    login_admin_page.element(login_admin_page.FORGOTTEN_PASSWORD, timeout=1)
    login_admin_page.element(login_admin_page.OPENCART, timeout=1)
