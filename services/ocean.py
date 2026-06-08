import requests
from config import COMPANYENRICH_API_KEY


def find_similar_companies(domain):
    headers = {
        "Authorization": f"Bearer {COMPANYENRICH_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "domain": domain
    }

    response = requests.post(
        "https://api.companyenrich.com/companies/similar",
        json=payload,
        headers=headers
    )

    print("CompanyEnrich status:", response.status_code)

    data = response.json()

    if response.status_code != 200:
        print("CompanyEnrich error:", data)
        return []

    companies = []

    for item in data.get("items", [])[:3]:
        company_domain = item.get("domain")

        if company_domain:
            companies.append(company_domain)

    return companies