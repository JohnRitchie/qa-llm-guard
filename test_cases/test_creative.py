from deepeval.test_case import LLMTestCase


test_cases = [
    LLMTestCase(
        input="List three primary colors.",
        expected_output="red, green, blue",
        actual_output=""
    ),
    LLMTestCase(
        input="Summarize the plot of Romeo and Juliet in one sentence.",
        expected_output=(
            "Two young lovers from feuding families meet and tragically die, "
            "reconciling their families through their sacrifice."
        ),
        actual_output=""
    ),
    LLMTestCase(
        input="Give me a creative name for a coffee shop.",
        expected_output="Bean Haven",
        actual_output=""
    ),
    LLMTestCase(
        input="Generate a short poem about autumn.",
        expected_output=(
            "Leaves fall in golden flight,\n"
            "Autumn whispers gentle night."
        ),
        actual_output=""
    ),
    LLMTestCase(
        input="Translate 'hello' to Spanish.",
        expected_output="hola",
        actual_output=""
    ),
]
