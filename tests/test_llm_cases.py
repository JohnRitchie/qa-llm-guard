import pytest
from deepeval import evaluate
import os
from dotenv import load_dotenv
from llm_guard.loader import load_all_test_cases
from llm_guard.models.openai_model import get_llm_response
from deepeval.metrics import AnswerRelevancyMetric
from llm_guard.metrics.local_embedding import LocalEmbeddingSimilarityMetric


load_dotenv()
DEFAULT_THRESHOLD = 0.8


all_cases = load_all_test_cases()

@pytest.mark.parametrize(
    "test_case",
    all_cases,
    ids=[test_case.input for test_case in all_cases]
)
def test_llm_case(test_case, cache):
    """
    Parametrized test: runs one LLMTestCase through the framework,
    uses cache if available, updates cache if --update-cache was passed,
    then evaluates with LocalEmbeddingSimilarityMetric
    """
    cache_key = test_case.input.strip()
    if cache_key in cache:
        test_case.actual_output = cache[cache_key]
    else:
        test_case.actual_output = get_llm_response(test_case)
        cache[cache_key] = test_case.actual_output

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        model_name = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        metric = AnswerRelevancyMetric(threshold=DEFAULT_THRESHOLD, model=model_name)
    else:
        # Local embedding similarity metric if no API key
        metric = LocalEmbeddingSimilarityMetric(threshold=DEFAULT_THRESHOLD)

    evaluate([test_case], [metric])
