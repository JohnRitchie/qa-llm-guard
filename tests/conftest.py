import pytest
from llm_guard.cache import load_cache, save_cache


def pytest_addoption(parser):
    parser.addoption(
        "--cached",
        action="store_true",
        default=False,
        help="Use cached LLM responses"
    )
    parser.addoption(
        "--update-cache",
        action="store_true",
        default=False,
        help="Update cache with new LLM responses"
    )


@pytest.fixture(scope="session")
def cache(request):
    """
    Session-scoped fixture that loads the cache if requested,
    and saves it at teardown if update-cache was passed.
    """
    use_cache = request.config.getoption("cached")
    update_cache = request.config.getoption("update_cache")
    cache_data = load_cache() if use_cache or update_cache else {}
    yield cache_data
    if update_cache:
        save_cache(cache_data)
