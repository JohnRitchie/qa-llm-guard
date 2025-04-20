from deepeval.test_case import LLMTestCase

test_cases = [
    LLMTestCase(
        input="What is the capital of France?",
        expected_output="Paris",
        actual_output="",
    ),
    LLMTestCase(
        input="What is the capital of Germany?",
        expected_output="Berlin",
        actual_output="",
    )
]
