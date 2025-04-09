from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey
from database.database import Base

class GoodsReceiptItems(Base):
    __tablename__ = "goods_receipt_items"
    id = Column(Integer, primary_key=True, index=True)
    goods_receipt_id = Column(Integer, ForeignKey("goods_receipts.id"), nullable=False)
    product_id= Column(Integer, ForeignKey("products.id"), nullable=False)
    qty_received = Column(Integer)