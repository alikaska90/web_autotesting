from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class DesktopsPage(BasePage):
    HEADING = (By.XPATH, '//h2[text()="Desktops"]')
    PRODUCT_COMPARE = (By.XPATH, '//*[@id="compare-total"]')
    SORT_BY_LIST = (By.XPATH, '//*[@id="input-sort"]')
    SHOW_LIST = (By.XPATH, '//*[@id="input-limit"]')
    LIST_VIEW = (By.XPATH, '//*[@id="list-view"]')
    GRID_VIEW = (By.XPATH, '//*[@id= "grid-view"]')

    def __init__(self, webdriver_object):
        super().__init__(webdriver_object)
        self.title = 'Desktops'

    def heading(self, **kwargs):
        return self.element(self.HEADING, **kwargs)
