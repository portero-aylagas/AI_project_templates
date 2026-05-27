# Agent Instructions

Preserve this project architecture:

```text
config -> schemas -> prompts -> llm_client -> graph -> storage -> web -> tests
```

## Core Rules

- Keep prompt text in `src/langgraph_agent/prompts/`.
- Keep provider-specific code behind `llm_client.py`.
- Validate external inputs, model outputs, graph state, stored state, and API
  responses with Pydantic schemas.
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
  provider failures, failed nodes, and invalid structured output.
- Do not log secrets, credentials, raw sensitive user data, or full provider
  payloads.

## LangGraph Workflow Rules

- Use the `Workflow Automation`, `AI Software Architecture`, `Prompt Quality`,
  `Structured Output`, and `Cost And Usage` categories when extending this
  template.
- Keep graph state typed and explicit.
- Keep each node responsible for one workflow step.
- Return structured state updates from nodes instead of mutating hidden global
  state.
- Test routing decisions, state transitions, terminal states, and failure paths.
- Keep deterministic business rules separate from model calls.
- Document any new node, edge, checkpoint, or human approval point in the
  architecture docs.
