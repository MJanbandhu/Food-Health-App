from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MealBase(BaseModel):
    food_name: str
    calories: int

class MealCreate(MealBase):
    pass

class MealResponse(MealBase):
    id: int
    user_id: int
    logged_at: datetime

    model_config = {"from_attributes": True}
