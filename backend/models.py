"""
Data Models Module

These models serve as the data transfer objects between the frontend, API endpoints, 
and business logic layers.

Models are organized into two main categories:
- Company Search: Models for searching companies by name
- Ethical Evaluation: Models for requesting and representing ethical scores

Note:
    This file includes a forward reference resolution (CompanySearchResponse.model_rebuild())
    required because CompanySearchResponse references EthicsScore which is defined later.
"""
from pydantic import BaseModel
from typing import Dict, Optional, Tuple

############################
# Company Search Models
############################
class CompanySearchRequest(BaseModel):
    query: str

class CompanySearchResponse(BaseModel):
    name: str = "N/A"
    company_id: str = "N/A"
    ethics_score: Optional["EthicsScore"] = None
    llm_response: Optional[str] = None


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