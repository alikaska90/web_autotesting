import pytest

from srv.constants import CURRENCY
from srv.pages.elements.top_element import Top
from srv.pages.main_page import MainPage
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_main_page(driver, base_url):
    driver.get(base_url)
    yield WebdriverObject(driver)


@pytest.fixture()
def webdriver_desktops(driver, base_url):
    driver.get(base_url+'/desktops')
    yield WebdriverObject(driver)


def check_prices_with_new_currency(main_page, currency):
    for product in main_page.products():
        product_name = main_page.product_name(product)
        product_prices = main_page.product_prices(product)
        wrong_prices = [price for price in product_prices if CURRENCY[currency] not in price]
        assert not wrong_prices, f'Incorrect prices {wrong_prices} of {product_name} for currency {currency}'


@pytest.mark.parametrize('currency', ['EUR', 'GBP', 'USD'])
def test_currency_main_page(webdriver_main_page, currency):
    Top.Currency(webdriver_main_page) \
        .change_currency(currency)
    check_prices_with_new_currency(MainPage(webdriver_main_page), currency)


@pytest.mark.parametrize('currency', ['EUR', 'GBP', 'USD'])
def test_currency_desktops_page(webdriver_desktops, currency):
    Top.Currency(webdriver_desktops) \
        .change_currency(currency)
    check_prices_with_new_currency(MainPage(webdriver_desktops), currency)
