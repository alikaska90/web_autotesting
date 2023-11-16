from selenium.webdriver.common.by import By

from srv.pages.base_page import BasePage


class ProductCardPage(BasePage):
    WISH_LIST = (By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    COMPARE_PRODUCT = (By.XPATH, '//button[@data-original-title="Compare this Product"]')
    QUANTITY = (By.XPATH, '//*[@id="input-quantity"]')
    ADD_TO_CART = (By.XPATH, '//*[@id="button-cart"]')
    WRITE_REVIEW = (By.LINK_TEXT, 'Write a review')
