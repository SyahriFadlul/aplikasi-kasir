from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base
from .pivot import UserRole, RolePermission

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    user_roles = relationship("UserRole", back_populates="role")
    role_permissions = relationship("RolePermission", back_populates="role")

    # users = relationship("User", secondary=UserRole, back_populates="roles")