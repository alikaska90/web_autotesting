import pytest

from srv.pages.catalog_desktop_page import CatalogDesktopPageElements
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/desktops')
    yield WebdriverObject(driver)


def test_catalog_desktop_page(webdriver_object):
    assert webdriver_object.title == 'Desktops'
    webdriver_object.wait_visible_element(CatalogDesktopPageElements.DESKTOP_TITLE, timeout=1)
    webdriver_object.wait_visible_element(CatalogDesktopPageElements.PRODUCT_COMPARE, timeout=1)
    webdriver_object.wait_visible_element(CatalogDesktopPageElements.SORT_BY_LIST, timeout=1)
    webdriver_object.wait_visible_element(CatalogDesktopPageElements.SHOW_LIST, timeout=1)
    webdriver_object.wait_visible_element(CatalogDesktopPageElements.LIST_VIEW_BUTTON, timeout=1)
    webdriver_object.wait_visible_element(CatalogDesktopPageElements.GRID_VIEW_BUTTON, timeout=1)
