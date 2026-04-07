from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.food import Meal
from app.schemas.meal import MealCreate, MealResponse

router = APIRouter()

@router.post("/track", response_model=MealResponse)
def track_meal(meal_in: MealCreate, db: Session = Depends(get_db)):
    # Standard MVP: Just dummy mapping to user_id=1
    db_meal = Meal(
        user_id=1, 
        food_name=meal_in.food_name, 
        calories=meal_in.calories
    )
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

@router.get("/dashboard", response_model=dict)
def get_dashboard(db: Session = Depends(get_db)):
    # Calculate dummy user stats
    meals = db.query(Meal).filter(Meal.user_id == 1).order_by(Meal.logged_at.desc()).all()
    total_calories = sum([m.calories for m in meals])
    goal = 2000
    alerts = []
    if total_calories > goal:
        alerts.append("Warning: You have exceeded your daily calorie goal!")
        
    return {
        "total_calories": total_calories,
        "daily_goal": goal,
        "recent_logs": [{"name": m.food_name, "calories": m.calories} for m in meals[:5]],
        "alerts": alerts
    }
