from deepeval.test_case import LLMTestCase


test_cases = [
    LLMTestCase(
        input="What is the capital of Ireland?",
        expected_output="Dublin",
        actual_output="",
        context=[
            "Imagine you're like wikipedia. I ask you a simple fact and you give me a succinct one-word answer"
        ]
    ),
    LLMTestCase(
        input="What is the capital of Germany?",
        expected_output="Berlin",
        actual_output="",
        context=[
            "Imagine you're like wikipedia. I ask you a simple fact and you give me a succinct one-word answer"
        ]
    )
]
