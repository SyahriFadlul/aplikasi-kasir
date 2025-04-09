from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey, Numeric, DateTime
from database.database import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    status = Column(Enum('pending', 'paid', 'processing', 'shipped', 'delivered', 'cancelled'), nullable=False, default='pending')
    discount = Column(Numeric(12, 2), nullable=True)
    tax = Column(Numeric(12, 2), nullable=True)
    shipping_cost = Column(Numeric(12, 2), nullable=True)
    total = Column(Numeric(12, 2), nullable=False)
    notes = Column(String(300))