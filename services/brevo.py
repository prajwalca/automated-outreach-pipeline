import requests
from config import BREVO_API_KEY


SENDER_EMAIL = "prajwal@helloprajwalca.online"
SENDER_NAME = "Prajwal"


def send_test_email():
    payload = {
        "sender": {
            "name": SENDER_NAME,
            "email": SENDER_EMAIL
        },
        "to": [
            {
                "email": "prajwalpraju.ca@gmail.com",
                "name": "Prajwal"
            }
        ],
        "subject": "Brevo API Test - Outreach Pipeline",
        "htmlContent": """
        <p>Hi Prajwal,</p>
        <p>This is a test email sent from the Outreach Pipeline using Brevo API.</p>
        <p>If you received this, Brevo integration is working.</p>
        """
    }

    headers = {
        "api-key": BREVO_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        json=payload,
        headers=headers
    )

    print("Brevo status:", response.status_code)
    print(response.text)


def send_emails(contacts):
    for contact in contacts:
        subject = f"Quick idea for {contact['company_domain']}"

        body = f"""
        <p>Hi {contact['name']},</p>

        <p>I noticed your work at {contact['company_domain']}.</p>

        <p>I am building an automated outreach pipeline that finds similar companies,
        discovers decision makers, and prepares personalized outreach emails.</p>

        <p>Would love to connect and share a quick idea.</p>

        <p>Regards,<br>Prajwal</p>
        """

        payload = {
            "sender": {
                "name": SENDER_NAME,
                "email": SENDER_EMAIL
            },
            "to": [
                {
                    "email": contact["email"],
                    "name": contact["name"]
                }
            ],
            "subject": subject,
            "htmlContent": body
        }

        headers = {
            "api-key": BREVO_API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            json=payload,
            headers=headers
        )

        print(f"Sending email to {contact['email']}")
        print("Brevo status:", response.status_code)
        print(response.text)
        print("-" * 50)