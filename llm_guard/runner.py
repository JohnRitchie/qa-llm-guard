from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric
from llm_guard.models.openai_model import get_llm_response
from llm_guard.loader import load_all_test_cases
from llm_guard.cache import load_cache, save_cache

def run_tests(use_cache=False, update_cache=False):
    """
    Runs LLM test cases using DeepEval, with optional caching support.
    """
    test_cases = load_all_test_cases()
    cache = load_cache() if use_cache or update_cache else {}

    for test_case in test_cases:
        cache_key = test_case.input.strip()

        if use_cache and cache_key in cache:
            test_case.actual_output = cache[cache_key]
        else:
            response = get_llm_response(test_case.input)
            test_case.actual_output = response
            if update_cache:
                cache[cache_key] = response

    if update_cache:
        save_cache(cache)

    metric = AnswerRelevancyMetric(threshold=0.8)
    evaluate(test_cases, [metric])
