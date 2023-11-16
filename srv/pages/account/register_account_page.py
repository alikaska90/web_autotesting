from selenium.webdriver.common.by import By

from srv.pages.account.data.account_data import RegistrationData
from srv.pages.base_page import BasePage


class RegisterAccountPage(BasePage):
    LOGIN_PAGE = (By.LINK_TEXT, 'login page')
    FIRSTNAME = (By.XPATH, '//*[@id="input-firstname"]')
    LASTNAME = (By.XPATH, '//*[@id="input-lastname"]')
    EMAIL = (By.XPATH, '//*[@id="input-email"]')
    PHONE = (By.XPATH, '//*[@id="input-telephone"]')
    PASSWORD = (By.XPATH, '//*[@id="input-password"]')
    PASSWORD_CONFIRM = (By.XPATH, '//*[@id="input-confirm"]')
    NEWSLETTER_YES = (By.XPATH, '//*[@name="newsletter"][@value="1"]')
    NEWSLETTER_NO = (By.XPATH, '//*[@name="newsletter"][@value="0"]')
    AGREE_POLICY = (By.XPATH, '//*[@name="agree"]')
    CONTINUE = (By.XPATH, '//*[@type="submit"][@value="Continue"]')

    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.title = 'Register Account'

    def fill_registration_form(self, data: RegistrationData):
        self.input(self.element(self.FIRSTNAME), data.firstname)
        self.input(self.element(self.LASTNAME), data.lastname)
        self.input(self.element(self.EMAIL), data.email)
        self.input(self.element(self.PHONE), data.phone)
        self.input(self.element(self.PASSWORD), data.password)
        self.input(self.element(self.PASSWORD_CONFIRM), data.password_confirm)
        return self

    def agree_to_privacy_policy(self):
        self.click(self.element(self.AGREE_POLICY))
        return self

    def click_continue(self):
        self.click(self.element(self.CONTINUE))

    def set_newsletter(self, yes=False):
        if yes:
            self.click(self.element(self.NEWSLETTER_YES))
            return self
        self.click(self.element(self.NEWSLETTER_NO))
        return self
