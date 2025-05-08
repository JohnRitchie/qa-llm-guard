import argparse
from llm_guard.runner import run_tests


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run LLM test cases.")
    parser.add_argument("--cached", action="store_true", help="Use cached LLM responses")
    parser.add_argument("--update-cache", action="store_true", help="Update LLM response cache")

    args = parser.parse_args()
    run_tests(use_cache=args.cached, update_cache=args.update_cache)
