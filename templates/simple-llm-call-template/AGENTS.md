# Agent Instructions

Preserve this project architecture:

```text
config -> schemas -> prompts -> llm_client -> workflow -> storage -> web -> tests
```

## Core Rules

- Keep prompt text in `src/simple_llm_call/prompts/`.
- Keep provider-specific code behind `llm_client.py`.
- Validate external inputs, model outputs, stored state, and API responses with
  Pydantic schemas.
- Use fake clients and deterministic fixtures in normal tests.
- Run `make verify` before reporting completion.
- Keep the starter GitHub Actions workflow lightweight and passing; it should
  install development dependencies and run `make verify`.
- Preserve Ruff linting and Google-style pydocstyle settings in
  `pyproject.toml`.
- Do not add live API keys, network-only checks, or paid services to normal
  verification or CI.

## Direct LLM Call Rules

- Keep this project as a direct-call architecture unless orchestration is truly
  required.
- Do not add LangChain, LangGraph, tools, or agent loops for one-step model
  tasks.
- Wrap raw model text in a typed response model before downstream use.
- Add tests for malformed, missing, or extra structured-output fields when
  changing schemas or response parsing.
- Keep prompt rendering explicit so user input is separated from instructions.
