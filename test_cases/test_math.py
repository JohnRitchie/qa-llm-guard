from deepeval.test_case import LLMTestCase


test_cases = [
    LLMTestCase(
        input="What is 2 + 2?",
        expected_output="4",
        actual_output=""
    ),
    LLMTestCase(
        input="What is 15 divided by 3?",
        expected_output="5",
        actual_output=""
    ),
    LLMTestCase(
        input="Solve for x: 2x + 3 = 7.",
        expected_output="2",
        actual_output=""
    ),
    LLMTestCase(
        input="What is the derivative of x^2?",
        expected_output="2x",
        actual_output=""
    ),
    LLMTestCase(
        input="What is the integral of 2x dx?",
        expected_output="x^2",
        actual_output=""
    ),
]
