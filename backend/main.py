from fastapi import FastAPI, Query
from models import CompanySearchRequest, CompanySearchResponse, EthicsScore, EthicsEvalRequest
from services import search_company, evaluate_ethics
from typing import Optional

app = FastAPI()

# App health check
@app.get("/health")
def health():
    return {"status": "ok"}

# Search for a company, and optionally ethics
@app.post("/search/text", response_model=CompanySearchResponse)
def search_by_text(req: CompanySearchRequest, eval: Optional[bool] = Query(False)):
    result = search_company(req.query)

    score = evaluate_ethics(result.company_id) if eval else None

    return CompanySearchResponse(
        name=result.name,
        company_id=result.company_id,
        ethics_score=score
    )

# Use a company ID to search for ethics
@app.post("/evaluate", response_model=EthicsScore)
def evaluate(request: EthicsEvalRequest):
    return evaluate_ethics(request.company_id)