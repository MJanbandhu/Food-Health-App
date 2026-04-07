from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class InitialFood(Base):
    # Dummy DB for standard food DB if needed
    __tablename__ = "foods"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    calories_per_serving = Column(Integer)
    protein = Column(Float, nullable=True)
    carbs = Column(Float, nullable=True)
    fat = Column(Float, nullable=True)


class Meal(Base):
    __tablename__ = "meals"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    food_name = Column(String, index=True)
    calories = Column(Integer)
    logged_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", backref="meals")
