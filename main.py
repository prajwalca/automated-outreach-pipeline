from services.ocean import find_similar_companies
from services.prospeo import find_contacts
from services.eazyreach import find_emails
from services.brevo import send_emails

domain = input("Enter seed company domain: ").strip()

if "." not in domain:
    print("Invalid domain. Please enter a proper domain like google.com")
    exit()

print("[1/4] Finding lookalike companies...")
companies = find_similar_companies(domain)

print("[2/4] Finding decision makers...")
contacts = find_contacts(companies)

print("[3/4] Resolving emails...")
emails = find_emails(contacts)

print("[4/4] Preparing outreach...")

print("\nSummary before sending:")
print(f"Companies found: {len(companies)}")
print(f"Contacts found: {len(contacts)}")
print(f"Emails found: {len(emails)}")

confirm = input("Send emails? yes/no: ")

if confirm.strip().lower() == "yes":
    send_emails(emails)
else:
    print("Email sending cancelled.")