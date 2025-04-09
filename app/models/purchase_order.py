from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey, DateTime
from database.database import Base

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    tax = Column(Enum('none', 'ppn'), default='none')
    discount = Column(Float, default=0.0)
    total_amount = Column(String(20), nullable=False)  
    status = Column(Enum('ordered', 'partial', 'received', 'pending'), default='pending')