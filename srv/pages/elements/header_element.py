from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class Header:
    """
    Elements in Header of page
    """

    class ShoppingCart(BasePage):
        SHOPPING_CART = (By.XPATH, '//*[@id="cart"]')
        CART_DROPDOWN = (By.XPATH, '//*[@class="dropdown-menu pull-right"]')
        PRODUCT_LIST = (By.XPATH, '//*[@class="table table-striped"]/tbody/tr')
        PRODUCT_NAME = (By.XPATH, './/*[@class="text-left"]/a')

        def open_shopping_cart(self):
            if not self.check_element_visibility(self.CART_DROPDOWN):
                self.element(self.SHOPPING_CART).click()
                self.element(self.CART_DROPDOWN)
            return self

        def products_in_cart(self):
            return self.elements(self.PRODUCT_LIST)

        def product_name(self, product):
            return product.find_element(*self.PRODUCT_NAME).text
