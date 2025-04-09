from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum
from database.database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)