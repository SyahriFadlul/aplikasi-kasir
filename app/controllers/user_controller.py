from app.database.database import SessionLocal
from app.models.user import User
from app.utils.security import hash_password\

import bcrypt


class Login:
    def __init__(self, User):
        self.user = User