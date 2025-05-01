
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_assets():
    response = client.get("/assets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_metrics():
    response = client.get("/metrics/BTC-USD")
    assert response.status_code == 200
    data = response.json()
    assert "latest_price" in data
    assert "change_percent_24h" in data
    assert "average_price_7d" in data

def test_compare_assets():
    response = client.get("/compare?asset1=BTC-USD&asset2=ETH-USD")
    assert response.status_code == 200
    data = response.json()
    assert "BTC-USD" in data
    assert "ETH-USD" in data
