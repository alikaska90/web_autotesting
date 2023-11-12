import random
import time

import pytest

from srv.pages.elements.top_element import Top
from srv.pages.elements.header_element import Header
from srv.pages.main_page import MainPage
from srv.pages.shopping_cart_page import ShoppingCartPage
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url)
    yield WebdriverObject(driver)


def random_index(i_min, i_max, disable: tuple):
    index = random.randint(i_min, i_max)
    if index in disable:
        return random_index(i_min, i_max, disable)
    return index


def test_shopping_cart(webdriver_object):
    main_page = MainPage(webdriver_object)

    products = main_page.products()
    rand = random_index(0, len(products)-1, (2, 3))
    random_product = products[rand]
    product_name_on_page = main_page.product_name(random_product)
    main_page.add_product_to_cart(random_product)

    # check product in cart dropdown menu
    header_shopping_cart = Header.ShoppingCart(webdriver_object)
    products_in_cart = header_shopping_cart \
        .open_shopping_cart() \
        .products_in_cart()
    assert len(products_in_cart) == 1, 'Incorrect number of products in cart'
    product_name_in_cart = header_shopping_cart.product_name(products_in_cart[0])
    assert product_name_on_page == product_name_in_cart

    # check product in cart on Shopping Cart page
    Top.ShoppingCart(webdriver_object).open_shopping_cart_page()
    shopping_cart_page = ShoppingCartPage(webdriver_object)
    assert webdriver_object.title == shopping_cart_page.title
    products_in_cart = shopping_cart_page.products_in_cart()
    assert len(products_in_cart) == 1, 'Incorrect number of products in cart'
    product_name_in_cart = shopping_cart_page.product_name(products_in_cart[0])
    assert product_name_on_page == product_name_in_cart
