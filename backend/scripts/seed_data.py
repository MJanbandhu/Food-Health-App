import sys
import os

# Add backend directory to sys path so we can import app modules properly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db.session import SessionLocal, engine, Base
from app.models.user import User
from app.models.food import InitialFood, Meal
from passlib.context import CryptContext
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Check if we already seeded to avoid duplicates
    if db.query(User).count() > 0:
        print("Database already seeded!")
        return

    print("Seeding dummy users...")
    user1 = User(
        email="testuser@example.com",
        full_name="John Doe",
        hashed_password=pwd_context.hash("password123"),
        daily_calorie_goal=2200
    )
    db.add(user1)
    db.commit()
    db.refresh(user1)

    print("Seeding dummy foods...")
    foods = [
        InitialFood(name="Apple", calories_per_serving=95, protein=0.5, carbs=25.0, fat=0.3),
        InitialFood(name="Grilled Chicken Breast", calories_per_serving=284, protein=53.4, carbs=0, fat=6.2),
        InitialFood(name="Quinoa Salad", calories_per_serving=222, protein=8.1, carbs=39.4, fat=3.6),
        InitialFood(name="Avocado Toast", calories_per_serving=350, protein=8.0, carbs=30.0, fat=22.0),
    ]
    db.add_all(foods)
    
    print("Seeding dummy meals (history)...")
    meals = [
        Meal(user_id=user1.id, food_name="Apple", calories=95, logged_at=datetime.utcnow() - timedelta(days=1)),
        Meal(user_id=user1.id, food_name="Grilled Chicken Breast", calories=284, logged_at=datetime.utcnow() - timedelta(hours=5)),
        Meal(user_id=user1.id, food_name="Avocado Toast", calories=350, logged_at=datetime.utcnow() - timedelta(hours=2)),
    ]
    db.add_all(meals)

    db.commit()
    db.close()
    print("Seeding complete! You can now log into the application with testuser@example.com / password123.")

if __name__ == "__main__":
    seed_database()
