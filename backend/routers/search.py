"""
Company Search Router Module

This module provides API routes for searching companies by name and optionally retrieving
their ethical evaluations in a single request.

Endpoints:
- POST /search/text: Search for a company by name with optional ethics evaluation

The router leverages the search_company and evaluate_ethics service functions to perform
the actual data retrieval and ethics scoring operations.
"""
from fastapi import APIRouter, Query
from backend.models import CompanySearchRequest, CompanySearchResponse
from backend.services import search_company, evaluate_ethics
from typing import Optional

search_router = APIRouter()

# Search for a company, and optionally ethics
@search_router.post("", response_model=CompanySearchResponse)
def search_by_text(req: CompanySearchRequest, eval: Optional[bool] = Query(False)):
    result = search_company(req.query)

    score = evaluate_ethics(result.company_id) if eval else None

    return CompanySearchResponse(
        name=result.name,
        company_id=result.company_id,
        ethics_score=score
    )