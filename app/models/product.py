from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey
from database.database import Base
from app.database.database import SessionLocal

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    barcode = Column(String(50))
    category_id = Column(Integer, ForeignKey('categories.id'))
    unit = Column(String(20))
    price = Column(Float)    
    promo_price = Column(Float)    
    stock = Column(Integer, default=0)
    alert_qty = Column(Integer, default=1)
    image = Column(String(255))
    is_featured = Column(Boolean, default=False)

    def to_dict(self):
        # return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return {
            # 'id': self.id,
            'Nama': self.name,
            'Barcode': self.barcode,
            'category_id': self.category_id,
            'unit': self.unit,
            'Harga': self.price,
            'Promo': self.promo_price,
            'Stok': self.stock,
            'Buffer Stok': self.alert_qty,
            'Gambar': self.image,
            'Ditampilkan': 'Ya' if self.is_featured else 'Tidak',
        }

    @staticmethod
    def create_product(data):
        print(data)
        with SessionLocal() as db:
            product = Product(
                name=data.get('name'),
                barcode=data.get('barcode'),
                category_id=data.get('category_id'),
                unit=data.get('unit'),
                price=data.get('price'),
                promo_price=data.get('promo_price'),
                stock=data.get('stock'),
                alert_qty=data.get('alert_qty'),
                image=data.get('image'),
                is_featured=data.get('is_featured', False)
            )
            db.add(product)
        
            db.commit()
            db.refresh(product)

        return product.to_dict()
        
    @staticmethod
    def get_all_products():
        with SessionLocal() as db:
            products = db.query(Product).all()
            return [p.to_dict() for p in products]

    @staticmethod
    def get_product_by_id(product_id: int):
        with SessionLocal() as db:
            product = db.query(Product).filter(Product.id == product_id).first()
        
        return product.to_dict() if product else None
    @staticmethod
    def update_product(product_id: int, data):
        with SessionLocal() as db:
            product = db.query(Product).filter(Product.id == product_id).first()
            if not product:
                return None
            
            for key, value in data.items():
                setattr(product, key, value)
            
            db.commit()
            db.refresh(product)
        
        return product.to_dict()
    @staticmethod
    def delete_product(product_id: int):
        with SessionLocal() as db:
            product = db.query(Product).filter(Product.id == product_id).first()
            if not product:
                return None
            
            db.delete(product)
            db.commit()
        
        return product.to_dict()
    @staticmethod
    def get_product_by_barcode(barcode: str):
        with SessionLocal() as db:
            product = db.query(Product).filter(Product.barcode == barcode).first()
        
        return product.to_dict() if product else None
    @staticmethod
    def get_product_by_name(name: str):
        with SessionLocal() as db:
            product = db.query(Product).filter(Product.name == name).first()
        
        return product.to_dict() if product else None
    @staticmethod
    def get_product_by_category(category_id: int):
        with SessionLocal() as db:
            products = db.query(Product).filter(Product.category_id == category_id).all()
        
        return [p.to_dict() for p in products] if products else None
