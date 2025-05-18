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
from datetime import datetime

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
    company_name: str
    category_tags: Optional[str]
    reasoning: Optional[str]
    sources: Optional[str]
    modified_time: Optional[datetime]
    scores: Dict[str, float]



# Resolve forward references at the end of the file
CompanySearchResponse.model_rebuild()