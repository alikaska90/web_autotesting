import pytest

from srv.pages.admin.admin_main_page import AdminMainPage
from srv.pages.admin.admin_products_page import AdminProductsPage
from srv.pages.admin.elements.add_edit_product import AddProduct
from srv.pages.admin.elements.product_list import ProductList
from srv.pages.admin.login_admin_page import LoginAdminPage
from srv.webdriver_object import WebdriverObject
from tests.hw2.test_data.new_product import ADD_GENERAL, ADD_DATA, ADD_LINKS, ADD_IMAGE, ADD_POINTS


@pytest.fixture()
def webdriver_object(driver, base_url):
    driver.get(base_url + '/admin')
    yield WebdriverObject(driver)


def test_create_delete_product(webdriver_object):
    login_admin_page = LoginAdminPage(webdriver_object)
    admin_main_page_menu = AdminMainPage.Menu(webdriver_object)
    admin_main_page_header = AdminMainPage.Header(webdriver_object)
    admin_products_page = AdminProductsPage(webdriver_object)
    add_product_page = AddProduct()
    product_list = ProductList(webdriver_object)

    # login
    login_admin_page.login()
    admin_main_page_menu.open_products_page()
    assert webdriver_object.title == admin_products_page.title
    admin_products_page.add_new()
    assert admin_products_page.panel_title() == add_product_page.panel_title

    # create new product
    add_product_page.General(webdriver_object).fill(ADD_GENERAL)
    add_product_page.Data(webdriver_object).fill(ADD_DATA)
    add_product_page.Links(webdriver_object).fill(ADD_LINKS)
    add_product_page.Image(webdriver_object).change_general_image(ADD_IMAGE)
    add_product_page.RewardPoints(webdriver_object).fill(ADD_POINTS)
    admin_products_page.save()
    assert add_product_page.alert in admin_products_page.alert()

    # delete product
    product = product_list.find_product_by_name(ADD_GENERAL.product_name)
    product_list.select_product(product)
    admin_products_page.delete(success=True)
    assert not product_list.check_product_in_list_by_name(ADD_GENERAL.product_name)

    # logout
    admin_main_page_header.logout()
