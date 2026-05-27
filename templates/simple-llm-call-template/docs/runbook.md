# Runbook

## Setup

Install the package with development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Copy `.env.example` to `.env` only for live runs. Tests do not need live keys.

## Verify

```bash
make verify
```

## Development Loop

1. Edit `schemas.py` to describe the data contract.
2. Edit `prompts/generation.md` to describe the model task.
3. Update `FakeLLMClient` so tests stay offline.
4. Add or update workflow tests.
5. Run `make verify`.

## Run Web UI

```bash
python -m simple_llm_call.web.app
```
