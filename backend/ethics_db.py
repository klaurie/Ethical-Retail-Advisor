from pymongo import MongoClient, ASCENDING
from datetime import datetime, timezone
from typing import Optional, Dict, Any


class EthicsDatabase:
    def __init__(self, db_url="mongodb://localhost:27017", db_name="ethical_db"):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db["company_profiles"]

        # Ensure uniqueness on company name
        self.collection.create_index([("company_name", ASCENDING)], unique=True)

    def create_or_update_company(self, company_name: str,
                                 category_tags: str,
                                 scores: Dict[str, float],
                                 reasoning: str,
                                 sources: str) -> bool:
        
        # Store input data
        data = {
            "company_name": company_name,
            "category_tags": category_tags,
            "scores": scores,
            "reasoning": reasoning,
            "sources": sources,
            "modified_time": datetime.now(timezone.utc).isoformat()
        }

        # Update or insert the company
        result = self.collection.update_one(
            {"company_name": company_name},
            {"$set": data},
            upsert=True
        )
        return result.modified_count > 0 or result.upserted_id is not None

    def get_company(self, company_name: str) -> Optional[Dict[str, Any]]:
        return self.collection.find_one({"company_name": company_name}, {"_id": 0})

    def delete_company(self, company_name: str) -> bool:
        result = self.collection.delete_one({"company_name": company_name})
        return result.deleted_count == 1

    def list_companies(self, limit: int = 10) -> list[Dict[str, Any]]:
        return list(self.collection.find({}, {"_id": 0}).limit(limit))

    def close(self):
        self.client.close()
