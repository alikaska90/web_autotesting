from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WebdriverObject:
    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.title

    def explicit_wait(self, method, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(method(locator))
        except TimeoutException:
            raise AssertionError(f'Element {locator} not found')

    def wait_visible_element(self, locator, **kwargs):
        return self.explicit_wait(EC.visibility_of_element_located, locator, **kwargs)

    def wait_visible_elements(self, locator, **kwargs):
        return self.explicit_wait(EC.visibility_of_all_elements_located, locator, **kwargs)

    def wait_element(self, locator, **kwargs):
        return self.explicit_wait(EC.presence_of_element_located, locator, **kwargs)

    def wait_clickable_element(self, locator, **kwargs):
        return self.explicit_wait(EC.element_to_be_clickable, locator, **kwargs)

    def wait_alert(self, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        except TimeoutException:
            raise AssertionError('Alert not found')
