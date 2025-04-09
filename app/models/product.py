from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey
from database.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    unit = Column(String(20))
    price = Column(Float)
    tax_type = Column(Enum('none', 'ppn'), default='none')
    barcode = Column(String(50))
    stock = Column(Integer, default=0)
    aler_qty = Column(Integer, default=0)
    is_featured = Column(Boolean, default=False)