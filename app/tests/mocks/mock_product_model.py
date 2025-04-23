

class MockProduct():
    def __init__(self):
        self.products = [
            {
                "id": 1,
                "name": "Kopi Kapal Api",
                "category_id": 1,
                "unit": "bks",
                "price": 2500,
                "tax_type": "p1",
                "barcode": "8991001101012",
                "stock": 100,
                "alert_qty": 10,
                "is_featured": True
            },
            {
                "id": 2,
                "name": "Indomie Goreng",
                "category_id": 2,
                "unit": "bks",
                "price": 3500,
                "tax_type": "",
                "barcode": "8992727000011",
                "stock": 200,
                "alert_qty": 20,
                "is_featured": True
            },
            {
                "id": 3,
                "name": "Teh Botol Sosro",
                "category_id": 3,
                "unit": "botol",
                "price": 5000,
                "tax_type": "p2",
                "barcode": "8996001300013",
                "stock": 80,
                "alert_qty": 10,
                "is_featured": False
            },
            {
                "id": 4,
                "name": "Aqua 600ml",
                "category_id": 3,
                "unit": "botol",
                "price": 3000,
                "tax_type": "p1",
                "barcode": "8996001000015",
                "stock": 150,
                "alert_qty": 15,
                "is_featured": False
            },
            {
                "id": 5,
                "name": "Rokok Djarum Super",
                "category_id": 4,
                "unit": "bungkus",
                "price": 25000,
                "tax_type": "p2",
                "barcode": "8999999111222",
                "stock": 60,
                "alert_qty": 10,
                "is_featured": True
            },
            {
                "id": 6,
                "name": "Chitato Sapi Panggang",
                "category_id": 5,
                "unit": "bks",
                "price": 7500,
                "tax_type": "",
                "barcode": "8998866100201",
                "stock": 90,
                "alert_qty": 10,
                "is_featured": False
            },
            {
                "id": 7,
                "name": "SilverQueen Chunky Bar",
                "category_id": 6,
                "unit": "pcs",
                "price": 12000,
                "tax_type": "p1",
                "barcode": "8991001223451",
                "stock": 40,
                "alert_qty": 5,
                "is_featured": True
            },
            {
                "id": 8,
                "name": "Pocari Sweat",
                "category_id": 3,
                "unit": "botol",
                "price": 7000,
                "tax_type": "p2",
                "barcode": "8997035566008",
                "stock": 70,
                "alert_qty": 10,
                "is_featured": False
            },
            {
                "id": 9,
                "name": "Good Day Cappuccino",
                "category_id": 1,
                "unit": "bks",
                "price": 2000,
                "tax_type": "",
                "barcode": "8991002100402",
                "stock": 100,
                "alert_qty": 10,
                "is_featured": False
            },
            {
                "id": 10,
                "name": "Beng Beng",
                "category_id": 6,
                "unit": "pcs",
                "price": 2000,
                "tax_type": "",
                "barcode": "8991001101234",
                "stock": 150,
                "alert_qty": 15,
                "is_featured": True
            },
            {
                "id": 11,
                "name": "Ultra Milk Coklat",
                "category_id": 3,
                "unit": "kotak",
                "price": 6000,
                "tax_type": "p1",
                "barcode": "8998009011121",
                "stock": 80,
                "alert_qty": 10,
                "is_featured": True
            },
            {
                "id": 12,
                "name": "Tic Tac",
                "category_id": 6,
                "unit": "bks",
                "price": 1500,
                "tax_type": "",
                "barcode": "8991001200411",
                "stock": 120,
                "alert_qty": 10,
                "is_featured": False
            },
            {
                "id": 13,
                "name": "Energen Coklat",
                "category_id": 1,
                "unit": "bks",
                "price": 2500,
                "tax_type": "p2",
                "barcode": "8998009011122",
                "stock": 90,
                "alert_qty": 10,
                "is_featured": True
            },
            {
                "id": 14,
                "name": "Roma Malkist",
                "category_id": 5,
                "unit": "bks",
                "price": 8000,
                "tax_type": "p1",
                "barcode": "8996001300042",
                "stock": 70,
                "alert_qty": 10,
                "is_featured": False
            },
            {
                "id": 15,
                "name": "Mizone Lychee Lemon",
                "category_id": 3,
                "unit": "botol",
                "price": 6000,
                "tax_type": "",
                "barcode": "8992745271283",
                "stock": 65,
                "alert_qty": 10,
                "is_featured": True
            },
        ]


    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for p in self.products:
            if p["id"] == product_id:
                return p
        return None
