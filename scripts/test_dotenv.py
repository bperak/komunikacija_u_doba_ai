import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Print the OPENAI_API_KEY
api_key = os.environ.get("OPENAI_API_KEY")
if api_key:
    # Print first 5 chars and last 4 chars for security
    print(f"API Key found: {api_key[:5]}...{api_key[-4:]}")
else:
    print("OPENAI_API_KEY not found in environment variables")

# Print all environment variables (optional)
print("\nAll environment variables:")
for key, value in os.environ.items():
    if key == "OPENAI_API_KEY":
        print(f"{key}: {value[:5]}...{value[-4:]}")
    elif "KEY" in key or "SECRET" in key:
        print(f"{key}: [REDACTED]")
    else:
        print(f"{key}: {value}") 