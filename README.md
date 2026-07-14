# hello-llm

Small Python project for learning LLM basics, built with [OpenRouter](https://openrouter.ai/) and [Pydantic](https://docs.pydantic.dev/).

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) for dependency management
- An `OPEN_ROUTER_KEY` environment variable set to your OpenRouter API key

## Setup

```bash
uv sync
export OPEN_ROUTER_KEY=your-key-here
```

## Scripts

- `main.py` — sends a basic chat completion request to OpenRouter.
- `extract.py` — extracts structured job posting data from raw text using a Pydantic schema and `response_format`.
- `build_prompt.py` — loads `jobs.json`, filters/ranks matching job postings, and builds a prompt for an LLM.
- `inbuilt.py` — standalone Python exercises using `TypedDict` and list/dict comprehensions (no LLM calls).

Run any script with:

```bash
uv run <script>.py
```
