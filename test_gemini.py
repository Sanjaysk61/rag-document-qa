import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# This finds .env no matter where you run the script from
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Hello Gemini! I am Sanjay, a Data Scientist. Tell me in 2 lines what RAG is."
)

print(response.text)