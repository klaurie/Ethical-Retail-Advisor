import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("status") == "ok"

@pytest.mark.parametrize("query,expected_name", [
    ("apple inc.", "Apple Inc."),
])
def test_search_text(query: str, expected_name: str):
    response = client.post("/search/text", json={"query": query})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data.get("name") == expected_name

def test_evaluate_endpoint():
    response = client.post("/evaluate", json={"company_id": "6829ffdf01512e40e2ad6042"})
    assert response.status_code == 200
    json_data = response.json()
    assert "scores" in json_data
    assert "category_tags" in json_data
    assert "reasoning" in json_data

def test_search_with_eval():
    response = client.post("/search/text?eval=true", json={"query": "aPPlE inC."})
    assert response.status_code == 200
    json_data = response.json()
    assert "ethics_score" in json_data
    assert json_data["ethics_score"] is not None
    assert json_data["ethics_score"].get("scores").get("overall") == 3.5
    # Print all the scores
    print("\n=== Retrieved Scores ===")
    print(f"Company Name: {json_data['name']}")
    for category, score in json_data["ethics_score"].get("scores").items():
        print(f"{category}: {score}")