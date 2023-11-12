from selenium.webdriver.common.by import By

from srv.pages.account.data.account_data import LoginData
from srv.pages.base_page import BasePage


class AccountLoginPage(BasePage):
    EMAIL = (By.XPATH, '//*[@id="input-email"]')
    PASSWORD = (By.XPATH, '//*[@id="input-password"]')
    LOGIN = (By.XPATH, '//input[@value="Login"]')

    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.title = 'Account Login'

    def fill_email(self, email=None):
        self.input(self.element(self.EMAIL), email)
        return self

    def fill_password(self, password=None):
        self.input(self.element(self.PASSWORD), password)
        return self

    def fill_login_form(self, data: LoginData):
        self.fill_email(data.email)
        self.fill_password(data.password)
        return self

    def click_login(self):
        self.click(self.element(self.LOGIN))
