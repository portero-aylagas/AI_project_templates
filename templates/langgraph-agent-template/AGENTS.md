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

## LangGraph Workflow Rules

- Keep graph state typed and explicit.
- Keep each node responsible for one workflow step.
- Return structured state updates from nodes instead of mutating hidden global
  state.
- Test routing decisions, state transitions, terminal states, and failure paths.
- Keep deterministic business rules separate from model calls.
- Document any new node, edge, checkpoint, or human approval point in the
  architecture docs.
