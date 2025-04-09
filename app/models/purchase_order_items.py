from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey
from database.database import Base

class PurchaseOrderItems(Base):
    __tablename__ = "purchase_order_items"
    id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey('purchase_orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    qty = Column(Integer, default=1)
    unit = Column(String(20))
    price= Column(Float, nullable=False)