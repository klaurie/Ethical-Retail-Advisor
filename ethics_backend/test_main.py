from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test endpoint available
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

# Test search functionality
def test_search_text():
    response = client.post("/search/text", json={"query": "apple"})
    assert response.status_code == 200
    assert response.json()["name"] == "Apple Inc."

# Check endpoints by evaluating the ethics of cmp-001
def test_evaluate_endpoint():
    response = client.post("/evaluate", json={"company_id": "cmp-001"})
    assert response.status_code == 200
    data = response.json()
    assert "overall_score" in data
    assert "categories" in data
    assert "sustainability" in data["categories"]

# Test a search with eval enabled
def test_search_with_eval():
    response = client.post("/search/text?eval=true", json={"query": "apple"})
    assert response.status_code == 200
    data = response.json()
    assert "ethics_score" in data
    assert data["ethics_score"] is not None
    assert data["ethics_score"]["overall_score"] == 7.2