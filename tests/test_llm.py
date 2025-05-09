import allure
from deepeval import evaluate
from llm_guard.loader import load_all_test_cases
from llm_guard.models.openai_model import get_llm_response
from llm_guard.metrics.local_embedding import LocalEmbeddingSimilarityMetric


DEFAULT_THRESHOLD = 0.8


@allure.suite("LLM Evaluation")
@allure.title("Evaluate all test cases with cached LLM responses")
def test_llm_responses(cache):
    """
    Runs all LLMTestCase through get_llm_response(),
    populates cache, then evaluates with LocalEmbeddingSimilarityMetric.
    """
    test_cases = load_all_test_cases()

    for test_case in test_cases:
        cache_key = test_case.input.strip()
        if cache_key in cache:
            test_case.actual_output = cache[cache_key]
        else:
            test_case.actual_output = get_llm_response(test_case)
            cache[cache_key] = test_case.actual_output

    metric = LocalEmbeddingSimilarityMetric(threshold=DEFAULT_THRESHOLD)
    evaluate(test_cases, [metric])
