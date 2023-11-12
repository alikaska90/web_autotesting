from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class MainPage(BasePage):
    PRODUCTS = (By.XPATH, '//*[contains(@class, "product-layout")]')
    PRODUCT_PRICES = (By.XPATH, './/*[@class="price"]')
    PRODUCT_NAME = (By.XPATH, './/*[@class="caption"]//a')
    PRODUCT_CART_ADD_BUTTON = (By.XPATH, './/*[contains(@onclick, "cart.add")]')
    PRODUCT_WISHLIST_BUTTON = (By.XPATH, './/*[contains(@onclick, "wishlist.add")]')
    PRODUCT_COMPARE_BUTTON = (By.XPATH, './/*[contains(@onclick, "compare.add")]')
    PICTURE_SLIDESHOW = (By.XPATH, '//*[@id="slideshow0"]')
    CAROUSEL_WITH_SPONSORS = (By.XPATH, '//*[@id="carousel0"]')

    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.title = 'Your Store'

    def products(self, **kwargs) -> list:
        return self.elements(self.PRODUCTS, **kwargs)

    def product_prices(self, product) -> list:
        """
        output:
            * [price, Ex Tax] if product has normal price;
            * [new price, old price, Ex Tax] if product has promotional price.
        """
        return list(product.find_element(*self.PRODUCT_PRICES).text.replace('Ex Tax:', '').split())

    def product_name(self, product) -> str:
        return product.find_element(*self.PRODUCT_NAME).text

    def add_product_to_cart(self, product):
        self.click(product.find_element(*self.PRODUCT_CART_ADD_BUTTON))
