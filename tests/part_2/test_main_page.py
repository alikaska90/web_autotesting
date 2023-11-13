import pytest

from srv.pages.main_page import MainPageElements
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url)
    yield WebdriverObject(driver)


def test_main_page(webdriver_object):
    assert webdriver_object.title == 'Your Store'
    webdriver_object.wait_visible_element(MainPageElements.PRODUCT_ON_PAGE, timeout=1)
    webdriver_object.wait_visible_element(MainPageElements.PRODUCT_CART_ADD_BUTTON, timeout=1)
    webdriver_object.wait_visible_element(MainPageElements.PRODUCT_WISHLIST_BUTTON, timeout=1)
    webdriver_object.wait_visible_element(MainPageElements.PICTURE_SLIDESHOW, timeout=1)
    webdriver_object.wait_visible_element(MainPageElements.CAROUSEL_WITH_SPONSORS, timeout=1)
