from selenium.webdriver.common.by import By


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
