import pytest

from srv.pages.main_page import MainPage
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url)
    yield WebdriverObject(driver)


def test_main_page(webdriver_object):
    main_page = MainPage(webdriver_object)
    assert webdriver_object.title == main_page.title
    main_page.products(timeout=1)
    main_page.element(main_page.PRODUCT_CART_ADD_BUTTON, timeout=1)
    main_page.element(main_page.PRODUCT_WISHLIST_BUTTON, timeout=1)
    main_page.element(main_page.PICTURE_SLIDESHOW, timeout=1)
    main_page.element(main_page.CAROUSEL_WITH_SPONSORS, timeout=1)
