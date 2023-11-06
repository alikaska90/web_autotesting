from selenium.webdriver.common.by import By


class ShoppingCartPageElements:
    PRODUCT_TABLE = (By.XPATH, '//*[@class="table-responsive"]')
    PRODUCT_IN_CART = (By.XPATH, './/tbody/tr')
    PRODUCT_NAME_IN_CART = (By.XPATH, './/*[@class="text-left"]/a')
