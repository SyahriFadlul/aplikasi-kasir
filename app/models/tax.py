from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey, Numeric
from database.database import Base

class Tax(Base):
    __tablename__ = "taxes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    rate = Column(Numeric(12, 2), nullable=False)
    # type = Column(String(50), nullable=False)