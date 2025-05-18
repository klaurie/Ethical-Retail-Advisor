import pytest
from backend.services import search_company, evaluate_ethics

# Test cases for the search_company function
@pytest.mark.parametrize("query,expected_name", [
    ("Apple Inc.", "Apple Inc."),
    ("Meta Platforms, Inc.", "Meta Platforms, Inc."),
    ("NonExistentCompany", "Unknown"),
])
def test_search_company(query, expected_name):
    result = search_company(query)
    assert result.name == expected_name
    assert isinstance(result.company_id, str)

# Test cases for the evaluate_ethics function
@pytest.mark.parametrize("company_id,expected_name,expected_scores", [
    ("6829ffdf01512e40e2ad6042", None, None),  # Known ObjectId (we test name exists)
    ("cmp-999", "Unknown", {}),                 # Non-existent cmp-### ID
])
def test_evaluate_ethics(company_id, expected_name, expected_scores):
    score = evaluate_ethics(company_id)
    if expected_name is not None:
        assert score.company_name == expected_name
    else:
        assert score.company_name != "Unknown"  # We expect a real company here
    if expected_scores is not None:
        assert score.scores == expected_scores
