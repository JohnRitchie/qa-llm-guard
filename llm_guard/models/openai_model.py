import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env into os.environ
load_dotenv()

# Load API key and model name from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

def get_llm_response(prompt: str) -> str:
    """
    Sends a prompt to the OpenAI Chat API and returns the model's response.
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
