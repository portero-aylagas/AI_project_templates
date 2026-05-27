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

## Shared Quality Rules

- Keep code beginner/intermediate-friendly with clear names, simple control
  flow, and explicit side effects at workflow, storage, provider, and web
  boundaries.
- Keep public modules, classes, and functions documented with concise
  Google-style docstrings.
- Raise useful error messages for missing configuration, malformed input,
  provider failures, and invalid structured output.
- Do not log secrets, credentials, raw sensitive user data, or full provider
  payloads.

## Direct LLM Call Rules

- Use the `Prompt Quality`, `Dynamic Prompting`, `Structured Output`,
  `LLM/API Integration`, and `Cost And Usage` categories when extending this
  template.
- Keep this project as a direct-call architecture unless orchestration is truly
  required.
- Do not add LangChain, LangGraph, tools, or agent loops for one-step model
  tasks.
- Wrap raw model text in a typed response model before downstream use.
- Add tests for malformed, missing, or extra structured-output fields when
  changing schemas or response parsing.
- Keep prompt rendering explicit so user input is separated from instructions.
