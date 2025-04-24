import os
from dotenv import load_dotenv
from openai import OpenAI
from transformers import pipeline

# Load .env into os.environ
load_dotenv()


def get_llm_response(prompt: str) -> str:
    """
    Sends a prompt to the OpenAI Chat API and returns the model's response.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        client = OpenAI(api_key=api_key)
        MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    else:
        # Локальная модель через Hugging Face
        gen = pipeline("text-generation", model=os.getenv("FALLBACK_MODEL"))
        return gen(prompt, max_length=100)[0]["generated_text"]
