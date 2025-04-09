from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum
from database.database import Base

class Unit(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
