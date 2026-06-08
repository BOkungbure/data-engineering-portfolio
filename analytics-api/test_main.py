from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Analytics API is live" in response.json()["message"]

def test_get_revenue():
    response = client.get("/metrics/revenue")
    assert response.status_code == 200
    assert "total_revenue" in response.json()

def test_get_revenue_by_region():
    response = client.get("/metrics/revenue/North")
    assert response.status_code == 200
    assert response.json()["region"] == "North"

def test_invalid_region():
    response = client.get("/metrics/revenue/Mars")
    assert response.status_code == 200
    assert "error" in response.json()

def test_get_summary():
    response = client.get("/metrics/summary")
    assert response.status_code == 200
    assert "data" in response.json()
