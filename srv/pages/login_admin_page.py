from selenium.webdriver.common.by import By


class LoginAdminPageElements:
    USERNAME = (By.ID, 'input-username')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, 'Forgotten Password')
    OPENCART = (By.XPATH, '//a[text()="OpenCart"]')
