from pydantic import BaseModel
from typing import Dict, Optional, Tuple

############################
# Company Search Models
############################
class CompanySearchRequest(BaseModel):
    query: str

class CompanySearchResponse(BaseModel):
    name: str
    company_id: str
    ethics_score: Optional["EthicsScore"] = None


############################
# Ethical Search Models
############################
class EthicsEvalRequest(BaseModel):
    company_id: str

class EthicsScore(BaseModel):
    overall_score: float

    # Ethics categories: name, score, and reasoning
    categories: Dict[str, Tuple[float, str]]


# Resolve forward references at the end of the file
CompanySearchResponse.model_rebuild()