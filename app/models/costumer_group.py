from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum
from database.database import Base

class CustomerGroup(Base):
    __tablename__ = "customer_groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)