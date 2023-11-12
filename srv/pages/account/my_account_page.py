from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class MyAccountPage(BasePage):
    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.title = 'My Account'
