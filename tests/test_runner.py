import allure
from llm_guard.runner import run_tests

@allure.suite("LLM Evaluation")
@allure.title("Evaluate all test cases with cached LLM responses")
def test_llm_responses_pass_with_cache():
    """
    Smoke test: runs all LLM test cases using the cache.
    """
    run_tests(use_cache=False, update_cache=False)
