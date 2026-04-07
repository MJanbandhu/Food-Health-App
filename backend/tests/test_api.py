import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Modular Food & Health Smart API"}

def test_recommendations_endpoint():
    response = client.get("/api/v1/recommendations/recommendations")
    assert response.status_code == 200
    assert "recommendations" in response.json()

def test_scanner_mock():
    response = client.post("/api/v1/scanner/scanner")
    assert response.status_code == 200
    data = response.json()
    assert "detected_food" in data
    assert "estimated_calories" in data
