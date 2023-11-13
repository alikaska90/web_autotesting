import pytest

from srv.pages.product_card_page import ProductCardPage
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/tablet/samsung-galaxy-tab-10-1')
    yield WebdriverObject(driver)


def test_product_card_page(webdriver_object):
    product_card_page = ProductCardPage(webdriver_object)
    assert webdriver_object.title == 'Samsung Galaxy Tab 10.1'
    product_card_page.element(product_card_page.WISH_LIST, timeout=1)
    product_card_page.element(product_card_page.COMPARE_PRODUCT, timeout=1)
    product_card_page.element(product_card_page.QUANTITY, timeout=1)
    product_card_page.element(product_card_page.ADD_TO_CART, timeout=1)
    product_card_page.element(product_card_page.WRITE_REVIEW, timeout=1)
