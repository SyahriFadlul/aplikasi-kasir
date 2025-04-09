from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base
from .pivot import RolePermission

class Permission(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)

    role_permissions = relationship("RolePermission", back_populates="permission")