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

    def fill_firstname(self, firstname=None):
        self.input(self.element(self.FIRSTNAME), firstname)
        return self

    def fill_lastname(self, lastname=None):
        self.input(self.element(self.LASTNAME), lastname)
        return self

    def fill_email(self, email=None):
        self.input(self.element(self.EMAIL), email)
        return self

    def fill_phone(self, phone=None):
        self.input(self.element(self.PHONE), phone)
        return self

    def fill_password(self, password=None):
        self.input(self.element(self.PASSWORD), password)
        return self

    def fill_password_confirm(self, password_confirm=None):
        self.input(self.element(self.PASSWORD_CONFIRM), password_confirm)
        return self

    def fill_registration_form(self, data: RegistrationData):
        self.fill_firstname(data.firstname) \
            .fill_lastname(data.lastname) \
            .fill_email(data.email) \
            .fill_phone(data.phone) \
            .fill_password(data.password) \
            .fill_password_confirm(data.password_confirm)
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
