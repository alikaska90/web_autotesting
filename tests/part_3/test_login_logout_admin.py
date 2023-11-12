import pytest

from srv.pages.admin.admin_main_page import AdminMainPage
from srv.pages.admin.login_admin_page import LoginAdminPage
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/admin')
    yield WebdriverObject(driver)


def test_login_logout_admin(webdriver_object):
    login_page = LoginAdminPage(webdriver_object)
    login_page.login()
    AdminMainPage.Header(webdriver_object) \
        .check_logout_button() \
        .logout()
    login_page.check_login_button()
    assert webdriver_object.title == login_page.title

