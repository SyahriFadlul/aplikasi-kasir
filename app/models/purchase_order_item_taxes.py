from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from database.database import Base

class PurchaseOrderItemTaxes(Base):
    __tablename__ = "purchase_order_item_taxes"
    id = Column(Integer, primary_key=True, index=True)
    po_item_id = Column(Integer, ForeignKey('purchase_order_items.id'), nullable=False)
    tax_name = Column(String(100), nullable=False)
    tax_rate = Column(Numeric(5, 2), nullable=False)
    tax_amount = Column(Numeric(15, 2), nullable=False)

    purchase_order_item = relationship("PurchaseOrderItems", back_populates="taxes")