from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class Top:
    """ Elements at Top of page """

    class Currency(BasePage):
        CURRENCY_BUTTON = (By.XPATH, '//*[@id="form-currency"]')
        CURRENCY_MENU = (By.XPATH, '//*[@id="form-currency"]//*[@class="dropdown-menu"]')

        def open_currency_dropdown_menu(self):
            if not self.check_element_visibility(self.CURRENCY_MENU):
                self.element(self.CURRENCY_BUTTON).click()
                self.element(self.CURRENCY_MENU)
            return self

        def change_currency(self, currency):
            self.open_currency_dropdown_menu()
            self.element((By.XPATH, f'//button[@name="{currency}"]')).click()
            return self

    class ShoppingCart(BasePage):
        SHOPPING_CART = (By.XPATH, '//*[@id="top-links"]//a[@title="Shopping Cart"]')

        def open_shopping_cart_page(self):
            self.element(self.SHOPPING_CART).click()

    class MyAccount(BasePage):
        MY_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="top-links"]//a[@title="My Account"]')
        ACCOUNT_MENU = (By.XPATH, '//*[@id="top-links"]//*[contains(@class, "dropdown-menu")]')
        LOGIN = (By.XPATH, '//*[@id="top-links"]//*[text()="Login"]')
        LOGOUT = (By.XPATH, '//*[@id="top-links"]//*[text()="Logout"]')

        def open_my_account_dropdown_menu(self):
            if not self.check_element_visibility(self.ACCOUNT_MENU):
                self.element(self.MY_ACCOUNT_BUTTON).click()
                self.element(self.ACCOUNT_MENU)
            return self

        def logout(self):
            self.open_my_account_dropdown_menu()
            self.element(self.LOGOUT).click()
            return self

        def open_login_form(self):
            self.open_my_account_dropdown_menu()
            self.element(self.LOGIN).click()
            return self
