from backend.models import EthicsScore, CompanySearchResponse

# Searches and returns a company name and id
def search_company(query: str):
    # TODO: Update dummy mapping with a database/web search
    mapping = {
        "apple": ("Apple Inc.", "cmp-001"),
        "microsoft": ("Microsoft Inc.", "cmp-002"),
    }

    name, cid = mapping.get(query.lower(), ("Unknown", "cmp-000"))
    return CompanySearchResponse(name=name, company_id=cid)

# Searches and returns a company ethical score
def evaluate_ethics(company_id: str) -> EthicsScore:
    # TODO: Update dummy mapping with a database/web search and eval
    return EthicsScore(
        overall_score=7.2,
        categories={
            "sustainability": (9.0, "Good practices in waste management"),
            "worker treatment": (5.0, "Average treatment of workers")
        }
    )