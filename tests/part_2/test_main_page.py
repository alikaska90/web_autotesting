import pytest

from srv.pages.main_page import MainPageElements
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url)
    yield WebdriverObject(driver)


def test_main_page(webdriver_object):
    assert webdriver_object.title == 'Your Store'
    webdriver_object.wait_visible_element(MainPageElements.CURRENCY_BUTTON, timeout=1)
    webdriver_object.wait_visible_element(MainPageElements.MENU, timeout=1)
    webdriver_object.wait_visible_element(MainPageElements.SEARCH_FIELD, timeout=1)
    webdriver_object.wait_visible_element(MainPageElements.SEARCH_BUTTON, timeout=1)
    webdriver_object.wait_visible_element(MainPageElements.FOOTER_MY_ACCOUNT, timeout=1)
