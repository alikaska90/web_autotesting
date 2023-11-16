import os

from srv.pages.admin.constants import TaxClass, StockStatus, WeightClass, Status
from srv.pages.admin.data.product_edit_form_data import ProductEditFormData

ADD_GENERAL = ProductEditFormData.General(
        product_name='iPhone 12 Pro Max 256GB',
        description_note='New iPhone 12 Pro Max',
        meta_tag_title='iPhone 12 Pro Max 256GB'
)

ADD_DATA = ProductEditFormData.Data(
        model='iPhone 12 Pro Max',
        price='750.00',
        tax_class=TaxClass.TAXABLE_GOODS,
        quantity='50',
        stock_status=StockStatus.IN_STOCK,
        weight='260',
        weight_class=WeightClass.GRAM,
        status=Status.ENABLED,
        sort_order='0'
)

ADD_LINKS = ProductEditFormData.Links(
        manufacturer='Apple',
        categories=('Phones & PDAs',)
)

ADD_IMAGE = ProductEditFormData.Images(
        path=os.path.join(os.path.dirname(__file__), 'iphone_12_pro_max.jpg'),
        image_name='iphone_12_pro'
)

ADD_POINTS = ProductEditFormData.RewardPoints(
        points='0',
        default='0'
)
