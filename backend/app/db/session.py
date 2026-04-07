from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings

# Temporary fallback logic to sqlite if Postgres is not spun up yet
engine = None
try:
    if settings.USE_SQLITE_FALLBACK:
        engine = create_engine(settings.SQLITE_URL, connect_args={"check_same_thread": False})
    else:
        engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
except Exception:
    engine = create_engine(settings.SQLITE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
