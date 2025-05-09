from deepeval.test_case import LLMTestCase


test_cases = [
    LLMTestCase(
        input="Write a Python function that reverses a string.",
        expected_output=(
            "def reverse_string(s):\n"
            "    return s[::-1]"
        ),
        actual_output=""
    ),
    LLMTestCase(
        input="How do you open a file named 'data.txt' for reading in Python?",
        expected_output="open('data.txt', 'r')",
        actual_output=""
    ),
    LLMTestCase(
        input="Write a for loop in JavaScript to log numbers 1 through 5.",
        expected_output=(
            "for (let i = 1; i <= 5; i++) {\n"
            "    console.log(i);\n"
            "}"
        ),
        actual_output=""
    ),
    LLMTestCase(
        input="How do you declare a constant in Go?",
        expected_output="const x = 10",
        actual_output=""
    ),
    LLMTestCase(
        input="Write a SQL query to select all columns from a table named users.",
        expected_output="SELECT * FROM users;",
        actual_output=""
    ),
]
