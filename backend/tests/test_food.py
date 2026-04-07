from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_track_food_dummy():
    pass
