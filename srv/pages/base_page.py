from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, webdriver_object):
        self.webdriver_object = webdriver_object
        self.driver = webdriver_object.driver

    def click(self, element):
        (ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform())

    def input(self, element, value):
        if not value:
            return
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element(self, locator: tuple, **kwargs):
        return self.webdriver_object.wait_visible_element(locator, **kwargs)

    def elements(self, locator: tuple, **kwargs):
        return self.webdriver_object.wait_visible_elements(locator, **kwargs)

    def invisible_element(self, locator: tuple, **kwargs):
        return self.webdriver_object.wait_element(locator, **kwargs)

    def select_by_value(self, locator: tuple, value, **kwargs):
        if not value:
            return
        select = Select(self.webdriver_object.wait_clickable_element(locator, **kwargs))
        return select.select_by_value(value)

    def check_element_visibility(self, locator: tuple, **kwargs) -> bool:
        element = self.webdriver_object.wait_element(locator, **kwargs)
        if element.is_displayed():
            return True
        return False

    def base_alert(self):
        alert = self.webdriver_object.wait_alert()
        alert.accept()

    def prompt_alert(self, accept=False):
        alert = self.webdriver_object.wait_alert()
        if accept:
            alert.accept()
            return
        alert.dismiss()
