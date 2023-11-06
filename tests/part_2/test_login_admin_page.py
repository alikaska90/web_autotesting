import pytest

from srv.pages.login_admin_page import LoginAdminPageElements
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/admin')
    yield WebdriverObject(driver)


def test_login_admin_page(webdriver_object):
    assert webdriver_object.title == 'Administration'
    webdriver_object.wait_visible_element(LoginAdminPageElements.USERNAME, timeout=1)
    webdriver_object.wait_visible_element(LoginAdminPageElements.PASSWORD, timeout=1)
    webdriver_object.wait_visible_element(LoginAdminPageElements.LOGIN_BUTTON, timeout=1)
    webdriver_object.wait_visible_element(LoginAdminPageElements.FORGOTTEN_PASSWORD, timeout=1)
    webdriver_object.wait_visible_element(LoginAdminPageElements.OPENCART, timeout=1)
