from selenium.webdriver.common.by import By


class CatalogDesktopPageElements:
    DESKTOP_TITLE = (By.XPATH, '//h2[text()="Desktops"]')
    PRODUCT_COMPARE = (By.XPATH, '//*[@id="compare-total"]')
    SORT_BY_LIST = (By.XPATH, '//*[@id="input-sort"]')
    SHOW_LIST = (By.XPATH, '//*[@id="input-limit"]')
    LIST_VIEW_BUTTON = (By.XPATH, '//*[@id="list-view"]')
    GRID_VIEW_BUTTON = (By.XPATH, '//*[@id= "grid-view"]')
