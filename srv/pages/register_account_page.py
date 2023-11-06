from selenium.webdriver.common.by import By


class RegisterAccountPageElements:
    LOGIN_PAGE = (By.LINK_TEXT, 'login page')
    FIRSTNAME_FIELD = (By.XPATH, '//*[@id="input-firstname"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="input-password"]')
    NEWSLETTER_YES = (By.XPATH, '//*[@name="newsletter"][@value="1"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@type="submit"][@value="Continue"]')
