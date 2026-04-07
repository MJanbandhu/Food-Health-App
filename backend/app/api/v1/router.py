from fastapi import APIRouter
from app.api.v1.endpoints import auth, food, scanner, recommendations

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(food.router, prefix="/food", tags=["food"])
api_router.include_router(scanner.router, prefix="/scanner", tags=["scanner"])
api_router.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
