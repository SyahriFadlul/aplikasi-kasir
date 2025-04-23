from app.models.product import Product

class ProductController:
    def __init__(self, model):
        self.model = model

    # def get_all_products(self, page=1, per_page=20, sort_by='name', search_query=None):
    def get_all_products(self):
        return self.model.get_all_products()

        return products

        # Filtering (by name or barcode misalnya)
        if search_query:
            products = [
                p for p in products if search_query.lower() in p['name'].lower() or search_query in p['barcode']
            ]

        # Sorting
        products = sorted(products, key=lambda x: x.get(sort_by))

        # Pagination
        start = (page - 1) * per_page
        end = start + per_page
        paginated = products[start:end]

        return paginated, len(products)  # return data + total count
