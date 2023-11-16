from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    PRODUCT_LIST = (By.XPATH, '//*[@class="table-responsive"]//tbody/tr')
    PRODUCT_NAME = (By.XPATH, './/*[@class="text-left"]/a')

    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.title = 'Shopping Cart'

    def products_in_cart(self):
        return self.elements(self.PRODUCT_LIST)

    def product_name(self, product):
        return product.find_element(*self.PRODUCT_NAME).text
