import requests
from config import PROSPEO_API_KEY, USE_MOCK_DATA


def find_contacts(companies):

    if USE_MOCK_DATA:
        return [
            {
                "company_domain": company,
                "name": "Sample Founder",
                "title": "Founder",
                "linkedin_url": f"https://linkedin.com/in/sample-{company}",
                "email": f"sample.founder@{company}"
            }
            for company in companies
        ]

    contacts = []

    for company in companies[:1]:
        payload = {
            "page": 1,
            "filters": {
                "company": {
                    "websites": {
                        "include": [company]
                    }
                }
            }
        }

        headers = {
            "X-KEY": PROSPEO_API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.post(
            "https://api.prospeo.io/search-person",
            json=payload,
            headers=headers
        )

        print("Prospeo status:", response.status_code)

        data = response.json()

        if data.get("error"):
            print("Prospeo error:", data)
            continue

        for item in data.get("results", [])[:3]:
            person = item.get("person", {})
            company_data = item.get("company", {})

            contacts.append({
                "person_id": person.get("id"),
                "company_domain": company,
                "name": person.get("full_name") or person.get("name"),
                "title": person.get("job_title"),
                "linkedin_url": person.get("linkedin_url"),
                "company_name": company_data.get("name")
            })

    return contacts