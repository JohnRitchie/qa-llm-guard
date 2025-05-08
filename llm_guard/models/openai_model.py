import os
from dotenv import load_dotenv
from openai import OpenAI
from transformers import pipeline
from deepeval.test_case import LLMTestCase

# Load .env into os.environ
load_dotenv()

DEFAULT_SYSTEM_PROMPT = (
    "You are a concise assistant. "
    "Answer the user's question as briefly as possible."
)


def get_llm_response(test_case: LLMTestCase) -> str:
    """
    Sends a prompt to the model and returns the model's response.
    """
    system = test_case.context or DEFAULT_SYSTEM_PROMPT
    user_prompt = test_case.input

    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        client = OpenAI(api_key=api_key)
        model_name = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        print(f'Using {model_name}')
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt},
        ]
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.0,
            max_tokens=16,
        )
        return response.choices[0].message.content.strip()

    else:
        # local model Hugging Face
        model_name = os.getenv("FALLBACK_MODEL", "distilgpt2")
        print(f'Using {model_name}')
        generator = pipeline(
            "text-generation",
            model=model_name,
            do_sample=False,
            temperature=0.0,
        )
        full_prompt = f"{system}\n\nQuestion: {user_prompt}\nAnswer:"
        out = generator(full_prompt, max_new_tokens=16)
        text = out[0]["generated_text"]
        reply = text[len(full_prompt):].strip()
        # return only the first non-empty line
        for line in reply.splitlines():
            if line.strip():
                return line.strip()
        return reply
