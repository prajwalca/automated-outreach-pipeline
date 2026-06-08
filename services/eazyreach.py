def find_emails(contacts):
    enriched_contacts = []

    for contact in contacts:
        email = contact["name"].lower().replace(" ", ".") + "@" + contact["company_domain"]

        enriched_contacts.append({
            "company_domain": contact["company_domain"],
            "name": contact["name"],
            "title": contact["title"],
            "linkedin_url": contact["linkedin_url"],
            "email": email
        })

    return enriched_contacts