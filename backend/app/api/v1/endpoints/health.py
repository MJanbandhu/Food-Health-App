from fastapi import APIRouter
from app.services.health_service import HealthService

router = APIRouter()

@router.get("/status")
def health_check():
    return {"status": "healthy", "service": "food-health-app-backend"}

@router.post("/analyze")
def analyze_user_health(total_calories: int, daily_goal: int):
    alerts = HealthService.analyze_health(total_calories, daily_goal)
    return {"alerts": alerts}
