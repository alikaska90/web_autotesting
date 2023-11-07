from selenium.webdriver.common.by import By


class MainPageElements:
    PRODUCT_ON_PAGE = (By.XPATH, '//*[contains(@class, "product-layout")]')
    PRODUCT_PRICE = (By.XPATH, '//*[@class="price"]')
    PRODUCT_NAME = (By.XPATH, './/*[@class="caption"]//a')
    PRODUCT_CART_ADD_BUTTON = (By.XPATH, './/*[contains(@onclick, "cart.add")]')
    PRODUCT_WISHLIST_BUTTON = (By.XPATH, './/*[contains(@onclick, "wishlist.add")]')
    PRODUCT_COMPARE_BUTTON = (By.XPATH, './/*[contains(@onclick, "compare.add")]')
    PICTURE_SLIDESHOW = (By.XPATH, '//*[@id="slideshow0"]')
    CAROUSEL_WITH_SPONSORS = (By.XPATH, '//*[@id="carousel0"]')
