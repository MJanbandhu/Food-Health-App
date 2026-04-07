from fastapi import APIRouter

router = APIRouter()

@router.get("/recommendations")
def get_recommendations():
    # Mock Vertex AI recommendation
    return {
        "recommendations": [
            "We recommend a light salad for dinner.",
            "Try adding more healthy fats like avocado.",
            "Drink 2 more glasses of water today."
        ]
    }
