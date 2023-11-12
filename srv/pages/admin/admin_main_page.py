import time

from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class AdminMainPage:
    class Header(BasePage):
        LOGOUT_BUTTON = (By.CSS_SELECTOR, 'a[href*="logout"]')

        def logout(self):
            self.click(self.element(self.LOGOUT_BUTTON))
            return self

        def check_logout_button(self):
            # logout button on page
            self.element(self.LOGOUT_BUTTON)
            return self

    class Menu(BasePage):
        CATALOG = (By.XPATH, '//*[@id="menu-catalog"]')
        CATALOG_MENU = (By.XPATH, '//*[@id="collapse1"]')
        PRODUCTS = (By.XPATH, '//*[@id="collapse1"]//a[text()="Products"]')

        def open_catalog_menu(self):
            if not self.check_element_visibility(self.CATALOG_MENU):
                self.click(self.element(self.CATALOG))
            return self

        def open_products_page(self):
            self.open_catalog_menu()
            self.click(self.element(self.PRODUCTS))
            return self
