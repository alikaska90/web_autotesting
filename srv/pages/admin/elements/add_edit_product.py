from selenium.webdriver.common.by import By

from srv.pages.admin.data.product_edit_form_data import ProductEditFormData
from srv.pages.base_page import BasePage


class ProductEditForm:
    class General(BasePage):
        GENERAL = (By.XPATH, '//*[text()="General"]')
        PRODUCT_NAME = (By.XPATH, '//*[@id="input-name1"]')
        DESCRIPTION_NOTE = (By.XPATH, '//*[@class="note-editable"]')
        META_TAG_TITLE = (By.XPATH, '//*[@id="input-meta-title1"]')
        META_TAG_DESCRIPTION = (By.XPATH, '//*[@id="input-meta-description1"]')
        PRODUCT_TAG = (By.XPATH, '//*[@id="input-tag1"]')

        def open_general_form(self):
            self.click(self.element(self.GENERAL))

        def fill(self, data: ProductEditFormData.General):
            self.open_general_form()
            self.input(self.element(self.PRODUCT_NAME), data.product_name)
            self.input(self.element(self.DESCRIPTION_NOTE), data.description_note)
            self.input(self.element(self.META_TAG_TITLE), data.meta_tag_title)
            self.input(self.element(self.META_TAG_DESCRIPTION), data.meta_tag_desc)
            self.input(self.element(self.PRODUCT_TAG), data.product_tag)

    class Data(BasePage):
        DATA = (By.XPATH, '//*[text()="Data"]')
        MODEL = (By.XPATH, '//*[@id="input-model"]')
        PRICE = (By.XPATH, '//*[@id="input-price"]')
        TAX_CLASS = (By.XPATH, '//*[@id="input-tax-class"]')
        QUANTITY = (By.XPATH, '//*[@id="input-quantity"]')
        STOCK_STATUS = (By.XPATH, '//*[@id="input-stock-status"]')
        DATE_AVAILABLE = (By.XPATH, '//*[@id="input-date-available"]')
        WEIGHT = (By.XPATH, '//*[@id="input-weight"]')
        WEIGHT_CLASS = (By.XPATH, '//*[@id="input-weight-class"]')
        STATUS = (By.XPATH, '//*[@id="input-status"]')
        SORT_ORDER = (By.XPATH, '//*[@id="input-sort-order"]')

        def open_data_form(self):
            self.click(self.element(self.DATA))

        def fill(self, data: ProductEditFormData.Data):
            self.open_data_form()
            self.input(self.element(self.MODEL), data.model)
            self.input(self.element(self.PRICE), data.price)
            self.select_by_value(self.element(self.TAX_CLASS), data.tax_class)
            self.input(self.element(self.QUANTITY), data.quantity)
            self.select_by_value(self.element(self.STOCK_STATUS), data.stock_status)
            self.input(self.element(self.WEIGHT), data.weight)
            self.select_by_value(self.element(self.WEIGHT_CLASS), data.weight_class)
            self.select_by_value(self.element(self.STATUS), data.status)
            self.input(self.element(self.SORT_ORDER), data.sort_order)

    class Links(BasePage):
        LINKS = (By.XPATH, '//*[text()="Links"]')
        MANUFACTURER = (By.XPATH, '//*[@id="input-manufacturer"]')
        CATEGORIES = (By.XPATH, '//*[@id="input-category"]')

        def open_links_form(self):
            self.click(self.element(self.LINKS))

        def set_manufacturer(self, value=None):
            if not value:
                return
            self.input(self.element(self.MANUFACTURER), value)
            self.click(self.element((By.XPATH, f'//a[contains(text(), "{value}")]')))

        def set_categories(self, values=None):
            if not values:
                return
            for value in values:
                self.input(self.element(self.CATEGORIES), value)
                self.click(self.element((By.XPATH, f'//a[contains(text(), "{value}")]')))

        def fill(self, data: ProductEditFormData.Links):
            self.open_links_form()
            self.set_manufacturer(data.manufacturer)
            self.set_categories(data.categories)

    class RewardPoints(BasePage):
        REWARD_POINTS = (By.XPATH, '//*[text()="Reward Points"]')
        POINTS = (By.XPATH, '//*[@id="input-points"]')
        DEFAULT = (By.XPATH, '//*[@name="product_reward[1][points]"]')

        def open_reward_points_form(self):
            self.click(self.element(self.REWARD_POINTS))

        def fill(self, data: ProductEditFormData.RewardPoints):
            self.open_reward_points_form()
            self.input(self.element(self.POINTS), data.points)
            self.input(self.element(self.DEFAULT), data.default)

    class Image(BasePage):
        IMAGE = (By.XPATH, '//*[text()="Image"]')
        GENERAL_IMAGE = (By.XPATH, '//*[@id="thumb-image"]')
        CHANGE_IMAGE = (By.XPATH, '//*[@id="button-image"]')
        FILE_MANAGER = (By.XPATH, '//*[@id="filemanager"]')
        UPLOAD = (By.XPATH, '//*[@id="button-upload"]')

        def open_image_form(self):
            self.click(self.element(self.IMAGE))

        def activate_image_uploader(self):
            js_code = """HTMLInputElement.prototype.click = function () {
                        if (this.type !== 'file') {
                        HTMLElement.prototype.click.call(this);}
                        }"""
            self.driver.execute_script(js_code)

        def upload(self, data: ProductEditFormData.Images):
            if self.driver.find_elements(By.XPATH, f'//*[contains(@title, "{data.image_name}")]'):
                return
            self.activate_image_uploader()
            self.click(self.element(self.UPLOAD))
            uploader = self.invisible_element((By.XPATH, '//*[@id="form-upload"]/input[@type="file"]'))
            uploader.send_keys(data.path)
            self.base_alert()

        def change_general_image(self, data: ProductEditFormData.Images):
            self.open_image_form()
            self.click(self.element(self.GENERAL_IMAGE))
            self.click(self.element(self.CHANGE_IMAGE))
            self.element(self.FILE_MANAGER)
            self.upload(data)
            self.click(self.element((By.XPATH, f'//*[contains(@title, "{data.image_name}")]')))


class AddProduct(ProductEditForm):
    def __init__(self):
        self.panel_title = 'Add Product'
        self.alert = 'Success: You have modified products!'


class EditProduct(ProductEditForm):
    def __init__(self):
        self.panel_title = 'Edit Product'
        self.alert = 'Success: You have modified products!'
