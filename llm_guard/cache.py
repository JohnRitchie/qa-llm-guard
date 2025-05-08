import os
import json


CACHE_FILE = "llm_guard/cache.json"


def load_cache():
    """
    Loads cached responses from disk if available.
    """
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(data):
    """
    Saves a dictionary of prompt → response to disk as JSON.
    """
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
