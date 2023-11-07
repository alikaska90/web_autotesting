import random

import pytest

from srv.pages.base_page import BasePage
from srv.pages.main_page import MainPageElements
from srv.pages.shopping_cart_page import ShoppingCartPageElements
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url)
    yield WebdriverObject(driver)


def test_shopping_cart(webdriver_object):
    driver = webdriver_object.driver
    assert webdriver_object.title == 'Your Store'

    # check products on main page
    products_on_page = driver.find_elements(*MainPageElements.PRODUCT_ON_PAGE)
    assert products_on_page, 'No products found on main page'

    random_id = random.randint(0, len(products_on_page)-1)
    # disable monitor and camera from sample
    while random_id in (2, 3):
        random_id = random.randint(0, len(products_on_page)-1)

    random_product = products_on_page[random_id]
    product_name = random_product.find_element(*MainPageElements.PRODUCT_NAME).text

    # check cart add button no product card
    cart_add_button = random_product.find_elements(*MainPageElements.PRODUCT_CART_ADD_BUTTON)
    assert cart_add_button, 'No card add button found in product card'
    cart_add_button[0].click()

    # check product in cart dropdown menu
    shopping_cart = webdriver_object.wait_visible_element(BasePage.Header.ShoppingCart.SHOPPING_CART)
    shopping_cart.click()
    cart_dropdown = webdriver_object.wait_visible_element(BasePage.Header.ShoppingCart.CART_DROPDOWN)
    product_in_cart = cart_dropdown.find_elements(*BasePage.Header.ShoppingCart.PRODUCT_IN_CART)
    assert len(product_in_cart) == 1, 'Incorrect number of products in cart'
    product_name_in_cart = product_in_cart[0].find_element(*BasePage.Header.ShoppingCart.PRODUCT_NAME_IN_CART).text
    assert product_name == product_name_in_cart

    # check product in cart on Shopping Cart page
    top_shopping_cart = webdriver_object.wait_visible_element(BasePage.Top.ShoppingCart.SHOPPING_CART)
    top_shopping_cart.click()
    assert webdriver_object.title == 'Shopping Cart'
    product_table = webdriver_object.wait_visible_element(ShoppingCartPageElements.PRODUCT_TABLE)
    product_in_cart = product_table.find_elements(*ShoppingCartPageElements.PRODUCT_IN_CART)
    assert len(product_in_cart) == 1, 'Incorrect number of products in cart'
    product_name_in_cart = product_in_cart[0].find_element(*ShoppingCartPageElements.PRODUCT_NAME_IN_CART).text
    assert product_name == product_name_in_cart
