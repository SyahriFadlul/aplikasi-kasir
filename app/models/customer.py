from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey
from database.database import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey('customer_groups.id'), nullable=False)
    phone_number = Column(String(18), nullable=True)