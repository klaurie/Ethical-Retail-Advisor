from fastapi import APIRouter
from backend.models import EthicsEvalRequest, EthicsScore
from backend.services import evaluate_ethics

evaluate_router = APIRouter()

# Use a company ID to search for ethics
@evaluate_router.post("", response_model=EthicsScore)
def evaluate(request: EthicsEvalRequest):
    return evaluate_ethics(request.company_id)