# Sample code for successful commit
import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

# Retrieve secrets using os.getenv()
AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")

def connect():
    # Retrieve the password from the environment
    password = os.getenv("APP_PASSWORD")
    
    if not password:
        raise ValueError("APP_PASSWORD not found in environment!")
        
    print("Connecting with secure password retrieval.")

# # Sample code for testing Gitleaks guardrails

# # 1. Standard API Key Pattern (e.g., AWS-style)
# AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
# AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# # 2. Generic high-entropy secret
# # Most scanners catch high-entropy strings assigned to 'secret' or 'token'


# # 3. Connection String with Credentials
# DATABASE_URL = "postgres://admin:HardCodedPassword123@localhost:5432/mydb"

# # 4. Hardcoded variable names that trigger keyword rules
# def connect_to_service():
#     api_key = "p8Q~XyZzA1b2c3d4e5f6g7h8i9" # Azure-like secret
#     password = "SuperSecretPassword!2026"
#     print("Testing connection...")
