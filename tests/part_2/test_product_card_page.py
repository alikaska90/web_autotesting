import pytest

from srv.pages.product_card_page import ProductCardElements
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/tablet/samsung-galaxy-tab-10-1')
    yield WebdriverObject(driver)


def test_product_card_page(webdriver_object):
    assert webdriver_object.title == 'Samsung Galaxy Tab 10.1'
    webdriver_object.wait_visible_element(ProductCardElements.WISH_LIST, timeout=1)
    webdriver_object.wait_visible_element(ProductCardElements.COMPARE_PRODUCT, timeout=1)
    webdriver_object.wait_visible_element(ProductCardElements.QUANTITY, timeout=1)
    webdriver_object.wait_visible_element(ProductCardElements.ADD_TO_CART, timeout=1)
    webdriver_object.wait_visible_element(ProductCardElements.WRITE_REVIEW, timeout=1)
