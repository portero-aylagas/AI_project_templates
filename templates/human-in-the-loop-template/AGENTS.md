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
  provider failures, invalid review decisions, and invalid structured output.
- Do not log secrets, credentials, raw sensitive user data, or full provider
  payloads.

## Human Review Rules

- Use the `Workflow Automation`, `AI Software Architecture`, `Prompt Quality`,
  `Structured Output`, and `Cost And Usage` categories when extending this
  template.
- AI drafts are not final until a human review decision is persisted.
- Preserve approve, edit, and reject as explicit state transitions.
- Keep review state and audit records separate from display output.
- Test approve, edit, reject, unknown draft, and persistence behavior.
- Do not bypass review gates for actions that affect users, files, messages, or
  external systems.
- Keep reviewer notes and edited content typed and traceable.

---

For quick technical review: this repository is best evaluated as reusable Applied AI Integration / AI Workflow Engineering patterns. It codifies the same approach described in my profile README into project templates that other projects or teams can reuse for controlled AI-assisted software delivery.