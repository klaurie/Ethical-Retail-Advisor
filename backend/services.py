"""
Backend Services Module

This module provides service functions for searching companies and evaluating their ethical scores.
It currently uses dummy data but is designed to be replaced with actual database or API calls.

Services:
- search_company: Find company information based on text query
- evaluate_ethics: Retrieve ethical scores and details for a given company

TODO:
- Replace dummy implementations with actual database or API integrations
- Add caching for performance optimization
- Implement comprehensive error handling
"""
from backend.models import EthicsScore, CompanySearchResponse
from backend.ethics_db import EthicsDatabase
from bson.objectid import ObjectId
from datetime import datetime

# Searches and returns a company name and generated ID
def search_company(query: str) -> CompanySearchResponse:
    db = EthicsDatabase()
    company_doc = db.collection.find_one(
        {"company_name": {"$regex": f"^{query}$", "$options": "i"}},  # case-insensitive exact match
        {"_id": 0, "company_name": 1}
    )
    db.close()

    if company_doc:
        company_name = company_doc["company_name"]
        company_id = f"cmp-{abs(hash(company_name)) % 1000:03d}"  # consistent fake ID
        return CompanySearchResponse(name=company_name, company_id=company_id)
    else:
        print(f"No company result found for '{query}'. Web search functionality not implemented yet.")
        return CompanySearchResponse(name="Unknown", company_id="cmp-000")

# Searches and returns a company name, ID and ethics score
def evaluate_ethics(company_id: str) -> EthicsScore:
    db = EthicsDatabase()
    
    # company_id expected as stringified ObjectId or cmp-### fake id
    try:
        # Try interpreting as ObjectId first
        obj_id = ObjectId(company_id)
        company_doc = db.collection.find_one({"_id": obj_id})
    except Exception:
        # Fallback: search by generated cmp-### id based on company_name hash
        all_companies = list(db.collection.find())
        company_doc = None
        for company in all_companies:
            gen_id = f"cmp-{abs(hash(company['company_name'])) % 1000:03d}"
            if gen_id == company_id:
                company_doc = company
                break
    
    db.close()
    
    if not company_doc:
        print(f"No ethical data found for {company_id}. Web search functionality not implemented yet")
        return EthicsScore(
            company_name="Unknown",
            category_tags=None,
            reasoning=None,
            sources=None,
            modified_time=None,
            scores={}
        )
    
    # Parse modified_time to datetime if it's string
    mod_time = company_doc.get("modified_time")
    if isinstance(mod_time, str):
        try:
            mod_time = datetime.fromisoformat(mod_time)
        except Exception:
            mod_time = None
    
    return EthicsScore(
        company_name=company_doc.get("company_name", "Unknown"),
        category_tags=company_doc.get("category_tags"),
        reasoning=company_doc.get("reasoning"),
        sources=company_doc.get("sources"),
        modified_time=mod_time,
        scores=company_doc.get("scores", {})
    )