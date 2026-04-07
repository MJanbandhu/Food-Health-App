from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_recommendation():
    response = client.get("/api/v1/recommendations/recommendations")
    assert response.status_code == 200
