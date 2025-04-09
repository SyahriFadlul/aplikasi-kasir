from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
from .pivot import UserRole
from app.utils.security import hash_password
from app.database.database import SessionLocal

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(75), unique=True, nullable=False)
    password = Column(String(75), nullable=False)

    # roles = relationship("Role", secondary=UserRole, back_populates="users")
    user_roles = relationship("UserRole", back_populates="user")
    def has_permission(self, perm_name):
        for role in self.roles:
            for perm in role.permissions:
                if perm.name == perm_name:
                    return True
        return False

def create_user(username, password):
    db = SessionLocal()

    # hashed_password = hash_password(password)
    # try:
    #     new_user = User(username=username, password=hashed_password)
    #     db.add(new_user)
    #     db.commit()
    #     db.refresh(new_user)
    #     return new_user
    # except Exception as e:
    #     db.rollback()
    #     print(f"Error: {e}")
    # finally:
    #     db.close()

    # Cek apakah username sudah ada
    existing_user = db.query(User).filter(User.username == username).first()
    print('user : ', existing_user)
    print('username : ', username)
    print('password : ', password)

    if existing_user:
        return {"success": False, "message": "Username sudah digunakan"}

    # Validasi tambahan (misalnya panjang username dan password)
    if len(username) < 3:
        return {"success": False, "message": "Username minimal 3 karakter"}
    if len(password) < 6:
        return {"success": False, "message": "Password minimal 6 karakter"}

    # Hash password & simpan
    hashed_pw = hash_password(password)
    print('hashnya : ', hashed_pw)
    # new_user = User(username=username, password=hashed_password)
    # db.add(new_user)
    # db.commit()
    db.close()

    return {"success": True, "username": username, "message": "User berhasil dibuat"}

def show_all_users():
    db = SessionLocal()

    users = db.query(User).all()
    print('testing : ', users)
    db.close()

    return users

def show_user():
    db = SessionLocal()

def update_user():
    db = SessionLocal()

def delete_user():
    db = SessionLocal()

