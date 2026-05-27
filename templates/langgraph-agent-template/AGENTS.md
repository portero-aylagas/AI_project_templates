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
- Do not require live API keys, network access, or paid services for normal
  verification.

## LangGraph Workflow Rules

- Keep graph state typed and explicit.
- Keep each node responsible for one workflow step.
- Return structured state updates from nodes instead of mutating hidden global
  state.
- Test routing decisions, state transitions, terminal states, and failure paths.
- Keep deterministic business rules separate from model calls.
- Document any new node, edge, checkpoint, or human approval point in the
  architecture docs.

