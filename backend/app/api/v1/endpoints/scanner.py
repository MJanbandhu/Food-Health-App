from fastapi import APIRouter
import random

router = APIRouter()

@router.post("/scanner")
def scan_food(image_url: str = None):
    # Mock AI vision
    mock_foods = [("Apple", 95), ("Pizza Slice", 285), ("Salad", 150), ("Burger", 500)]
    food = random.choice(mock_foods)
    return {"detected_food": food[0], "estimated_calories": food[1]}
