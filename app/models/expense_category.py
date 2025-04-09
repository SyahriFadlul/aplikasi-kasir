from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey
from database.database import Base

class ExpenseCategory(Base):
    __tablename__ = "expense_categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    