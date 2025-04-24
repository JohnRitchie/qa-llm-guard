import os
from dotenv import load_dotenv
from openai import OpenAI
from transformers import pipeline

# Load .env into os.environ
load_dotenv()


def get_llm_response(prompt: str) -> str:
    """
    Sends a prompt to the model and returns the model's response.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        client = OpenAI(api_key=api_key)
        model_name = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        print(f'Using {model_name}')
        response = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    else:
        # local model Hugging Face
        model_name = os.getenv("FALLBACK_MODEL", "distilgpt2")
        print(f'Using {model_name}')
        generator = pipeline("text-generation", model=model_name)
        result = generator(prompt, max_length=100)
        return result[0]["generated_text"]
