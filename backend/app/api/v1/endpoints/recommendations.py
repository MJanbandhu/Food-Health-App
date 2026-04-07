from fastapi import APIRouter
from app.ai.vertex_ai_client import vertex_client

router = APIRouter()

@router.get("/recommendations")
def get_recommendations():
    # Attempt to use Vertex AI
    recs = vertex_client.get_smart_recommendations()
    return {"recommendations": recs}
