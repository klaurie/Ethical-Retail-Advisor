from ethics_db import EthicsDatabase
from datetime import datetime

example_data = [
    {
        "company_name": "Apple Inc.",
        "category_tags": "electronics, consumer tech, labor, environment",
        "scores": {
            "overall": 3.5,
            "labor": 3.0,
            "environment": 4.0,
            "transparency": 3.5
        },
        "reasoning": "Efforts in renewable energy and recycling, but ongoing concerns about overseas labor conditions.",
        "sources": "https://www.apple.com/environment/, https://www.theguardian.com/apple-labor",
    },
    {
        "company_name": "Microsoft Corporation",
        "category_tags": "software, cloud, carbon neutral, diversity",
        "scores": {
            "overall": 4.2,
            "labor": 4.0,
            "environment": 4.5,
            "transparency": 4.1
        },
        "reasoning": "Strong environmental initiatives and public commitments to carbon negativity. Generally transparent practices.",
        "sources": "https://www.microsoft.com/sustainability, https://ethics.microsoft.com",
    },
    {
        "company_name": "Amazon.com, Inc.",
        "category_tags": "e-commerce, logistics, labor, environment",
        "scores": {
            "overall": 2.8,
            "labor": 2.2,
            "environment": 3.5,
            "transparency": 2.7
        },
        "reasoning": "Invests in sustainability tech, but widely criticized for labor practices and warehouse conditions.",
        "sources": "https://sustainability.aboutamazon.com/, https://www.nytimes.com/amazon-labor",
    },
    {
        "company_name": "Alphabet Inc. (Google)",
        "category_tags": "search, ads, AI, green energy, privacy",
        "scores": {
            "overall": 3.9,
            "labor": 4.0,
            "environment": 4.4,
            "transparency": 3.2
        },
        "reasoning": "Carbon neutral data centers and major renewable investments, but concerns around data privacy and ad ethics.",
        "sources": "https://sustainability.google/, https://www.eff.org/google-transparency",
    },
    {
        "company_name": "Meta Platforms, Inc.",
        "category_tags": "social media, privacy, misinformation, AI",
        "scores": {
            "overall": 2.5,
            "labor": 3.5,
            "environment": 3.8,
            "transparency": 1.8
        },
        "reasoning": "Environmentally decent, but very low marks on privacy, content moderation, and transparency.",
        "sources": "https://sustainability.fb.com/, https://www.wsj.com/facebook-whistleblower",
    },
]


db = EthicsDatabase()

for entry in example_data:
    entry["modified_time"] = datetime.utcnow().isoformat()
    db.create_or_update_company(
        company_name=entry["company_name"],
        category_tags=entry["category_tags"],
        scores=entry["scores"],
        reasoning=entry["reasoning"],
        sources=entry["sources"]
    )

print("Example data inserted.")
db.close()
