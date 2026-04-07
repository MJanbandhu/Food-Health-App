import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.session import engine, Base
# Import all models so metadata knows about them
from app.models import user, food, health_log

def create_tables():
    print("Creating all database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()
