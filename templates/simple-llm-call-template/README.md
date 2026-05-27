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

## After Copying

This template is meant to become a fresh project. After copying it, rename the
project in `pyproject.toml`, rename `src/simple_llm_call/`, update imports in
`src/` and `tests/`, then run verification before adding real provider code.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
make verify
```

## File Map

- `src/simple_llm_call/config.py`: environment settings with fake-safe
  defaults.
- `src/simple_llm_call/schemas.py`: request, model-output, and workflow
  contracts.
- `src/simple_llm_call/prompts/generation.md`: the named prompt template.
- `src/simple_llm_call/llm_client.py`: fakeable provider boundary.
- `src/simple_llm_call/workflow.py`: prompt rendering and orchestration.
- `src/simple_llm_call/web/app.py`: thin FastAPI form that calls the workflow.
- `tests/`: fake-client and fixture tests that should stay offline.

## Customize First

Start by changing the schemas and prompt for your actual task. Then update the
fake client so tests describe the output shape you expect. Add a real provider
client only after the fake path and workflow tests are stable.

Avoid adding agents, tools, or retrieval here unless the task no longer fits a
direct model call. In that case, copy a more specific template instead.

## Run

```bash
python -m simple_llm_call.web.app
```

## Verify

```bash
make verify
```
