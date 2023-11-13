from srv.pages.admin.constants import TaxClass, StockStatus, WeightClass, Status


class ProductEditFormData:
    class General:
        def __init__(self,
                     product_name: str = None,
                     description_note: str = None,
                     meta_tag_title: str = None,
                     meta_tag_desc: str = None,
                     product_tag: str = None):
            self.product_name = product_name
            self.description_note = description_note
            self.meta_tag_title = meta_tag_title
            self.meta_tag_desc = meta_tag_desc
            self.product_tag = product_tag

    class Data:
        def __init__(self,
                     model: str = None,
                     price: str = None,
                     tax_class: TaxClass = None,
                     quantity: str = None,
                     stock_status: StockStatus = None,
                     weight: str = None,
                     weight_class: WeightClass = None,
                     status: Status = None,
                     sort_order: str = None):
            self.model = model
            self.price = price
            self.tax_class = tax_class
            self.quantity = quantity
            self.stock_status = stock_status
            self.weight = weight
            self.weight_class = weight_class
            self.status = status
            self.sort_order = sort_order

    class Links:
        def __init__(self,
                     manufacturer: str = None,
                     categories: tuple = None):
            self.manufacturer = manufacturer
            self.categories = categories

    class Images:
        def __init__(self,
                     path: str,
                     image_name: str):
            self.path = path
            self.image_name = image_name

    class RewardPoints:
        def __init__(self,
                     points: str = None,
                     default: str = None):
            self.points = points
            self.default = default
