"""
Ethics Evaluation Router Module

This module provides API routes for evaluating the ethical scores of companies.
It exposes a POST endpoint that accepts a company ID and returns comprehensive 
ethical evaluation data.

Endpoints:
- POST /evaluate: Evaluate ethics for a company based on its ID
"""
from fastapi import APIRouter
from backend.models import EthicsEvalRequest, EthicsScore
from backend.services import evaluate_ethics

evaluate_router = APIRouter()

# Use a company ID to search for ethics
@evaluate_router.post("", response_model=EthicsScore)
def evaluate(request: EthicsEvalRequest):
    return evaluate_ethics(request.company_id)