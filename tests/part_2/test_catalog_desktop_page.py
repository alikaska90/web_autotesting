import pytest

from srv.pages.catalog.desktop_page import DesktopsPage
from srv.webdriver_object import WebdriverObject


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/desktops')
    yield WebdriverObject(driver)


def test_catalog_desktop_page(webdriver_object):
    desktop_page = DesktopsPage(webdriver_object)
    assert webdriver_object.title == desktop_page.title
    desktop_page.heading(timeout=1)
    desktop_page.element(desktop_page.PRODUCT_COMPARE, timeout=1)
    desktop_page.element(desktop_page.SORT_BY_LIST, timeout=1)
    desktop_page.element(desktop_page.SORT_BY_LIST, timeout=1)
    desktop_page.element(desktop_page.SHOW_LIST, timeout=1)
    desktop_page.element(desktop_page.LIST_VIEW, timeout=1)
    desktop_page.element(desktop_page.GRID_VIEW, timeout=1)
