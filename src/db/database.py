import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Пытаемся получить полный URL, либо собираем из компонентов
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    user = os.getenv("POSTGRESQL_USER", "postgres")
    password = os.getenv("POSTGRESQL_PASSWORD", "admin")
    host = os.getenv("POSTGRESQL_HOST", "localhost")
    port = os.getenv("POSTGRESQL_PORT", "5432")
    db = os.getenv("POSTGRESQL_DB", "mydb")
    DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from src.db import models
    Base.metadata.create_all(bind=engine)