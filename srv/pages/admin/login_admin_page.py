from selenium.webdriver.common.by import By

from srv.pages.admin.constants import AdminCreds
from srv.pages.base_page import BasePage


class LoginAdminPage(BasePage):
    USERNAME = (By.ID, 'input-username')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    OPENCART = (By.XPATH, '//a[text()="OpenCart"]')

    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.title = 'Administration'

    def login(self):
        self.input(self.element(self.USERNAME), AdminCreds.USERNAME)
        self.input(self.element(self.PASSWORD), AdminCreds.PASSWORD)
        self.click(self.element(self.LOGIN_BUTTON))
        return self

    def check_login_button(self):
        # login button on page
        self.element(self.LOGIN_BUTTON)
