from selenium.webdriver.common.by import By


class Header:
    """
    Elements in Header of page
    """

    class ShoppingCart:
        SHOPPING_CART = (By.XPATH, '//*[@id="cart"]')
        CART_DROPDOWN = (By.XPATH, '//*[@class="dropdown-menu pull-right"]')
        PRODUCT_IN_CART = (By.XPATH, '//*[@class="table table-striped"]/tbody/tr')
        PRODUCT_NAME_IN_CART = (By.XPATH, './/*[@class="text-left"]/a')
