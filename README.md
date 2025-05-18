# QA-LLM Guard 🛡️

Automated testing framework for Large Language Models (LLMs), using [DeepEval](https://github.com/confident-ai/deepeval).

## 📑 Table of Contents

- [🚀 Overview](#overview)
- [🌟 Features](#features)
- [🛠️ Installation](#installation)
- [🏗️ Running tests](#running-tests)
- [📚 Directory Structure](#directory-structure)
- [📜 License](#license)

## Overview

This project helps you:
- Define structured test cases for LLMs in Python
- Evaluate model responses using a local embedding-based metric
- Run tests via pytest with optional response caching
- Get detailed Allure reports for each test case

## Features

✅ LLM test cases defined in Python  
✅ Local embedding similarity metric (offline)  
✅ OpenAI API support (configurable model)  
✅ Fallback to Hugging Face models if no API key  
✅ Response caching for faster repeat runs  
✅ Parametrized pytest suite with Allure integration

## Installation

```bash
git clone https://github.com/your-username/qa-llm-guard.git
cd qa-llm-guard
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env      # and fill in your OPENAI_API_KEY and OPENAI_MODEL if needed
```

## Running tests
Execute the full test suite and generate an Allure report:

```bash
pytest --update-cache   # fill or update response cache
pytest --cached         # run using cached responses
```
- --cached — use cached LLM responses
- --update-cache — update cache with new LLM responses

Allure results are written to allure-results/. To view the report locally, run:

```bash
allure serve allure-results
```

## Directory Structure

```bash
qa-llm-guard/
├── llm_guard/              # Core logic
│   ├── loader.py
│   ├── cache.py
│   ├── models/
│   │   └── openai_model.py
│   └── metrics/
│       └── local_embedding.py
├── test_cases/             # LLMTestCase definitions
│   ├── test_geography.py
│   ├── test_math.py
│   ├── test_programming.py
│   ├── test_history.py
│   └── test_creative.py
├── tests/
│   ├── conftest.py         # pytest options and cache fixture
│   └── test_llm_cases.py   # parametrized test for each case
├── requirements.txt
├── .env.example
├── pytest.ini
└── README.md

```

## License
MIT License