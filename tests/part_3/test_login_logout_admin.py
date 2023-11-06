import pytest

from srv.constants import ADMIN_USERNAME, ADMIN_PASSWORD
from srv.pages.admin_main_page import AdminMainPageElements
from srv.pages.login_admin_page import LoginAdminPageElements
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/admin')
    yield WebdriverObject(driver)


def test_login_logout_admin(webdriver_object):
    assert webdriver_object.title == 'Administration'
    # login
    username = webdriver_object.wait_visible_element(LoginAdminPageElements.USERNAME)
    username.click()
    username.send_keys(ADMIN_USERNAME)
    password = webdriver_object.wait_visible_element(LoginAdminPageElements.PASSWORD)
    password.click()
    password.send_keys(ADMIN_PASSWORD)
    webdriver_object.wait_visible_element(LoginAdminPageElements.LOGIN_BUTTON).click()

    # check login
    assert webdriver_object.title == 'Dashboard'
    # there is logout button
    logout = webdriver_object.wait_visible_element(AdminMainPageElements.LOGOUT_BUTTON)

    # logout
    logout.click()

    # check logout
    # there are form title "Please enter your login details." and login button
    webdriver_object.wait_visible_element(LoginAdminPageElements.FORM_TITLE)
    webdriver_object.wait_visible_element(LoginAdminPageElements.LOGIN_BUTTON)
