from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Enum, ForeignKey, Numeric, func
from database.database import Base
from app.database.database import SessionLocal

class PurchaseOrderItems(Base):
    __tablename__ = "purchase_order_items"
    id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey('purchase_orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    qty = Column(Integer, default=1)
    unit = Column(String(20))
    price= Column(Numeric(12, 2), nullable=False)
    tax_percent = Column(Numeric(12, 2), nullable=True)
    is_tax_inclusive = Column(Boolean, default=False)


    @staticmethod
    def get_all_items():
        with SessionLocal() as db:
            items = db.query(PurchaseOrderItems).all()
            # return [item.to_dict() for item in items]

        return items
    
    @staticmethod
    def get_item_by_id(item_id: int):
        with SessionLocal() as db:
            item = db.query(PurchaseOrderItems).filter(PurchaseOrderItems.id == item_id).first()
        
        return item
        # return item.to_dict() if item else None

    @staticmethod
    def calculate_po_total(po_id: int):
        with SessionLocal() as db:
            total = db.query(
                func.sum(
                    (PurchaseOrderItems.price * PurchaseOrderItems.qty) *
                    (1 + (func.coalesce(PurchaseOrderItems.tax_percent, 0) / 100))
                )
            ).filter(PurchaseOrderItems.po_id == po_id).scalar()
        total = db.query(
            func.sum(
                (PurchaseOrderItems.price * PurchaseOrderItems.qty) *
                (1 + (func.coalesce(PurchaseOrderItems.tax_percent, 0) / 100))
            )
        ).filter(PurchaseOrderItems.po_id == po_id).scalar()

        return float(total or 0.0)