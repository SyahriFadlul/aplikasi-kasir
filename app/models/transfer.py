from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey, Numeric, DateTime
from database.database import Base

class Transfer(Base):
    __tablename__ = "transfers"
    id = Column(Integer, primary_key=True, index=True)
    from_store = Column(String(100), nullable=False)
    to_store = Column(String(100), nullable=False)
    status = Column(Enum('pending', 'sent', 'receive'), default='pending')
    shipping_cost = Column(Numeric(12, 2), nullable=True)
    created_at= Column(DateTime)