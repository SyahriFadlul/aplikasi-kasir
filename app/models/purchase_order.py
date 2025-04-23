from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey, DateTime
from database.database import Base

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    status = Column(Enum('ordered', 'partial', 'received', 'pending'), default='pending')
    order_date = Column(DateTime, nullable=False)
    arrival_date = Column(DateTime, nullable=False)
    notes = Column(String(300))  
    discount = Column(Float, default=0.0)
    shipping_cost = Column(Float, default=0.0)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    updated_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    updated_at = Column(DateTime, nullable=False)