from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class CreatedAccountPage(BasePage):
    CONTINUE = (By.XPATH, '//*[@class="pull-right"]/a[text()="Continue"]')

    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.title = 'Your Account Has Been Created!'

    def click_continue(self):
        self.click(self.element(self.CONTINUE))
