import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

# Load .env
BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(dotenv_path=BASE_DIR / ".env", override=True)

# Read API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

# Create client
client = Groq(
    api_key=api_key
)


def generate_answer(prompt: str):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content