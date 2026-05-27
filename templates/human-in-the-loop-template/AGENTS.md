# Agent Instructions

Preserve this project architecture:

```text
config -> schemas -> prompts -> llm_client -> workflow -> storage -> web -> tests
```

## Core Rules

- Keep prompt text in `src/human_loop/prompts/`.
- Keep provider-specific code behind `llm_client.py`.
- Validate external inputs, model outputs, review decisions, stored state, and
  API responses with Pydantic schemas.
- Use fake clients and deterministic fixtures in normal tests.
- Run `make verify` before reporting completion.
- Do not require live API keys, network access, or paid services for normal
  verification.

## Human Review Rules

- AI drafts are not final until a human review decision is persisted.
- Preserve approve, edit, and reject as explicit state transitions.
- Keep review state and audit records separate from display output.
- Test approve, edit, reject, unknown draft, and persistence behavior.
- Do not bypass review gates for actions that affect users, files, messages, or
  external systems.
- Keep reviewer notes and edited content typed and traceable.

