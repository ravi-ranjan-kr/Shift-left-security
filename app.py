# # Dummy Azure secret (intentional)
# #AZURE_CLIENT_SECRET = "abcd1234-super-secret-key"
# AZURE_CLIENT_SECRET = "p8Q~XyZzA1b2c3d4e5f6g7h8i9"

# def connect():
#     password = "HardCodedPassword123"
#     print("Connecting with password:", password)

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
