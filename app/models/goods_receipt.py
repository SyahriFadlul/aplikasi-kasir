from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey, Date
from database.database import Base

class GoodsReceipt(Base):
    __tablename__ = "goods_receipts"
    id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey('purchase_orders.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)
    sj_number = Column(String(100))
    received_date = Column(Date, nullable=False)
    status = Column(Enum('ordered', 'partial', 'received', 'pending'), default='pending')
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)