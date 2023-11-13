from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class AdminProductsPage(BasePage):
    ADD_NEW = (By.XPATH, '//*[@data-original-title="Add New"]')
    DELETE = (By.XPATH, '//*[@data-original-title="Delete"]')
    PANEL_TITLE = (By.XPATH, '//*[@class="panel-title"]')
    SAVE = (By.XPATH, '//*[@data-original-title="Save"]')
    ALERT = (By.XPATH, '//*[contains(@class, "alert-success")]')

    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.title = 'Products'

    def panel_title(self):
        return self.element(self.PANEL_TITLE).text

    def add_new(self):
        self.click(self.element(self.ADD_NEW))
        return self

    def delete(self, success=False):
        self.click(self.element(self.DELETE))
        self.prompt_alert(accept=success)

    def save(self):
        self.click(self.element(self.SAVE))
        return self

    def alert(self):
        return self.element(self.ALERT).text
