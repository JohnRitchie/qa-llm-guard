from deepeval.test_case import LLMTestCase


test_cases = [
    LLMTestCase(
        input="In which year did the Battle of Hastings take place?",
        expected_output="1066",
        actual_output=""
    ),
    LLMTestCase(
        input="Who was the first President of the United States?",
        expected_output="George Washington",
        actual_output=""
    ),
    LLMTestCase(
        input="What year did the Berlin Wall fall?",
        expected_output="1989",
        actual_output=""
    ),
    LLMTestCase(
        input="Who discovered America in 1492?",
        expected_output="Christopher Columbus",
        actual_output=""
    ),
    LLMTestCase(
        input="What empire was ruled by Genghis Khan?",
        expected_output="Mongol Empire",
        actual_output=""
    ),
]
