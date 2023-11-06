from selenium.webdriver.common.by import By


class MainPageElements:
    def __init__(self, currency='USD'):
        self.currency = currency

    def change_currency(self):
        return By.XPATH, f'//button[@name="{self.currency}"]'

    CURRENCY_BUTTON = (By.XPATH, '//*[@id="form-currency"]')
    CURRENCY_MENU = (By.XPATH, '//*[@id="form-currency"]//*[@class="dropdown-menu"]')
    MENU = (By.XPATH, '//*[@id="menu"]')
    SEARCH_FIELD = (By.XPATH, '//*[@name="search"]')
    SEARCH_BUTTON = (By.XPATH, '//span[@class="input-group-btn"]')
    FOOTER_MY_ACCOUNT = (By.XPATH, '//body/footer//h5[text()="My Account"]')
    PRODUCT_PRICE = (By.XPATH, '//*[@class="price"]')
    PRODUCT_ON_PAGE = (By.XPATH, '//*[contains(@class, "product-layout")]')
    PRODUCT_NAME = (By.XPATH, './/*[@class="caption"]//a')
    PRODUCT_CART_ADD_BUTTON = (By.XPATH, './/*[contains(@onclick, "cart.add")]')
    HEADER_SHOPPING_CART = (By.XPATH, '//*[@id="cart"]')
    CART_DROPDOWN = (By.XPATH, '//*[@class="dropdown-menu pull-right"]')
    PRODUCT_IN_CART = (By.XPATH, './/*[@class="table table-striped"]/tbody/tr')
    PRODUCT_NAME_IN_CART = (By.XPATH, './/*[@class="text-left"]/a')
    TOP_SHOPPING_CART = (By.XPATH, '//*[@title="Shopping Cart"]')
