from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey
from database.database import Base
from app.database.database import SessionLocal

class Barcode(Base):
    __tablename__ = "barcodes"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(30), nullable=False)
    brand = Column(String(100))
    unit = Column(String(20))
    price = Column(Float)
    tax_type = Column(Enum('none', 'ppn'), default='none')
    barcode = Column(String(50))
    stock = Column(Integer, default=0)
    aler_qty = Column(Integer, default=0)
    is_featured = Column(Boolean, default=False)