import pytest

from srv.constants import CURRENCY
from srv.pages.main_page import MainPageElements
from srv.webdriver_object import WebdriverObject


@pytest.mark.parametrize('currency', ['EUR', 'GBP', 'USD'])
@pytest.mark.parametrize('url', ['', '/desktops'], ids=['main page', 'catalog desktop page'])
def test_currency_main_and_catalog_pages(driver, base_url, url, currency):
    driver.get(base_url + url)
    if url:
        assert driver.title == 'Desktops'
    else:
        assert driver.title == 'Your Store'
    webdriver_object = WebdriverObject(driver)
    main_page_elements = MainPageElements(currency)
    webdriver_object.wait_visible_element(main_page_elements.CURRENCY_BUTTON).click()
    # check currency menu
    webdriver_object.wait_visible_element(main_page_elements.CURRENCY_MENU)
    # choose currency
    webdriver_object.wait_visible_element(main_page_elements.change_currency()).click()
    # check currency of product prices
    prices_by_products = driver.find_elements(*main_page_elements.PRODUCT_PRICE)
    for product in prices_by_products:
        product_prices = list(product.text.replace('Ex Tax:', '').split())
        wrong_prices = [price for price in product_prices if CURRENCY[currency] not in price]
        assert not wrong_prices, f'Incorrect prices {wrong_prices} on page for currency {currency}'
