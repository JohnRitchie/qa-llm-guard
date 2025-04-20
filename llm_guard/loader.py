import importlib.util
import os
from deepeval.test_case import LLMTestCase

def load_test_cases_from_file(file_path: str) -> list[LLMTestCase]:
    """
    Dynamically loads LLMTestCase[] from a Python file.
    """
    spec = importlib.util.spec_from_file_location("test_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "test_cases", [])


def load_all_test_cases(test_cases_dir="test_cases") -> list[LLMTestCase]:
    """
    Loads all test cases from Python files in the given directory.
    """
    cases = []
    for filename in os.listdir(test_cases_dir):
        if filename.endswith(".py"):
            filepath = os.path.join(test_cases_dir, filename)
            cases += load_test_cases_from_file(filepath)
    return cases
