from dotenv import load_dotenv
import os

load_dotenv()

USE_MOCK_DATA = os.getenv("USE_MOCK_DATA", "true").lower() == "true"

COMPANYENRICH_API_KEY = os.getenv("COMPANYENRICH_API_KEY")
OCEAN_API_KEY = os.getenv("OCEAN_API_KEY")
PROSPEO_API_KEY = os.getenv("PROSPEO_API_KEY")
EAZYREACH_API_KEY = os.getenv("EAZYREACH_API_KEY")
BREVO_API_KEY = os.getenv("BREVO_API_KEY")
