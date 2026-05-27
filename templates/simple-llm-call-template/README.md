# Simple LLM Call Template

Use this template for AI features that are best implemented as direct model
calls: classification, extraction, rewriting, summarization, and small report
generation.

This is a software template, not a throwaway prompt demo. It separates prompts,
schemas, provider calls, workflow logic, storage, UI, tests, and documentation
so future changes can be inspected and verified safely.

## Quality Intent

- Model outputs are parsed into Pydantic schemas before downstream use.
- Prompt text lives in `src/simple_llm_call/prompts/`.
- Provider calls live behind `llm_client.py`.
- Tests use fake clients and fixtures, not live API keys.
- `make verify` is the normal local verification command.

## Run

```bash
python -m simple_llm_call.web.app
```

## Verify

```bash
make verify
```

