from selenium.webdriver.common.by import By


class BasePage:
    class Top:
        """
        Elements at Top of page
        """
        class Currency:
            CURRENCY_BUTTON = (By.XPATH, '//*[@id="form-currency"]')
            CURRENCY_MENU = (By.XPATH, '//*[@id="form-currency"]//*[@class="dropdown-menu"]')

            def __init__(self, currency='USD'):
                self.currency = currency

            def change_currency(self):
                return By.XPATH, f'//button[@name="{self.currency}"]'

        class ShoppingCart:
            SHOPPING_CART = (By.XPATH, '//*[@title="Shopping Cart"]')

    class Header:
        """
        Elements in Header of page
        """
        class ShoppingCart:
            SHOPPING_CART = (By.XPATH, '//*[@id="cart"]')
            CART_DROPDOWN = (By.XPATH, '//*[@class="dropdown-menu pull-right"]')
            PRODUCT_IN_CART = (By.XPATH, '//*[@class="table table-striped"]/tbody/tr')
            PRODUCT_NAME_IN_CART = (By.XPATH, './/*[@class="text-left"]/a')
