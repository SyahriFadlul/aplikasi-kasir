from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey, Numeric, DateTime
from database.database import Base

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    sale_date = Column(DateTime, default=DateTime.now, nullable=False)
    status = Column(Enum('draft', 'completed', 'canceled'), default='draft')
    discount = Column(Numeric(12, 2), nullable=True)
    tax = Column(Numeric(12, 2), nullable=True)
    shipping_cost = Column(Numeric(12, 2), nullable=True)
    notes = Column(String(300))
    payment_method = Column(String(50), nullable=False)
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    updated_by = Column(Integer, ForeignKey('users.id'), nullable=True)
    updated_at = Column(DateTime, nullable=True)