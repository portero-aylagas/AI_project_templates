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

## Run Web UI

```bash
python -m simple_llm_call.web.app
```

