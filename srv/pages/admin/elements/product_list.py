import time

from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class ProductList(BasePage):
    CHECKBOX = (By.XPATH, './/input[@type="checkbox"]')

    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.panel_title = 'Product List'
        self.alert = 'Success: You have modified products!'

    def product_name_locator(self, name):
        return By.XPATH, f"//*[@class='text-left'][1][text()='{name}']"

    def find_product_by_name(self, name):
        product_name = self.element(self.product_name_locator(name))
        return product_name.find_element(By.XPATH, './..')

    def set_checkbox(self, element):
        checkbox = element.find_element(*self.CHECKBOX)
        if not checkbox.is_selected():
            self.click(checkbox)

    def select_product(self, element):
        self.set_checkbox(element)

    def check_product_in_list_by_name(self, name):
        if self.driver.find_elements(*self.product_name_locator(name)):
            return True
        return False
