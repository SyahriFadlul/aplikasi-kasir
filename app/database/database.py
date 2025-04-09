import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
import os
from config import DATABASE_URL

load_dotenv()

engine = create_engine(DATABASE_URL, echo=True)

if not database_exists(engine.url):
    print("Database belum ada, sedang dibuat...")
    create_database(engine.url)
    print("Database berhasil dibuat.")

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
