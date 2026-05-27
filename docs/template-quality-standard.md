# Template Quality Standard

These templates encode two kinds of quality: software engineering quality and
AI engineering quality. Both are required for projects that integrate models,
tools, retrieval, or approval workflows.

## Engineering Quality

- Keep architecture readable: UI, workflow, prompts, provider calls, storage,
  configuration, and utilities have clear boundaries.
- Keep functions focused: one responsibility, clear names, explicit side
  effects, and Google-style docstrings for public modules, classes, and
  functions.
- Validate external data: user input, uploaded files, JSON, API responses,
  model outputs, and stored state must be parsed into typed schemas before
  downstream use.
- Handle errors deliberately: missing environment variables, file failures,
  malformed JSON, bad user input, and API failures should produce useful
  messages.
- Preserve testability: core workflow code accepts fake clients and fixtures
  instead of constructing live services internally.
- Keep repository hygiene: no virtual environments, caches, generated runtime
  outputs, secrets, or large local artifacts committed.
- Document reviewer evidence: setup, run command, verification command, sample
  input, expected output, limitations, and fallback behavior.

## AI Engineering Quality

- Prompts have stable names, explicit inputs, clear constraints, and documented
  output format.
- Dynamic prompt variables are separated from instructions and inserted through
  one prompt-rendering path.
- Structured outputs are validated with Pydantic before they are trusted.
- Provider calls are isolated behind narrow wrappers that centralize model
  names, temperature, timeouts, retries, token limits, and parsing.
- Normal tests use fake model clients, fake tools, fake embeddings, or fixture
  responses. They do not require live API keys, network access, or paid
  services.
- RAG pipelines separate loading, chunking, embedding, retrieval, ranking, and
  answer generation.
- Agents expose tool names, descriptions, typed inputs, typed outputs, failure
  behavior, and traceable tool-call logs.
- Workflow automation uses explicit state, run IDs, idempotency, retries,
  failure branches, approvals where needed, and recovery notes.
- Logs are useful for debugging but must not include secrets, credentials, or
  sensitive user data.
- Evaluation starts small: representative fixtures, expected answer properties,
  expected retrieved document IDs, and manual review notes for subjective
  quality.

## Required Files

Every template includes:

```text
README.md
PROJECT_SPEC.md
AGENTS.md
.env.example
Makefile
verify.sh
pyproject.toml
.github/workflows/verify.yml
src/<package>/config.py
src/<package>/schemas.py
src/<package>/llm_client.py
src/<package>/storage.py
src/<package>/prompts/
src/<package>/web/
tests/fakes/
tests/fixtures/
docs/architecture.md
docs/runbook.md
docs/limitations.md
docs/evaluation.md
```

## Verification Gates

- `make verify` is the fast repository gate. It checks required structure plus
  static acceptance basics: non-empty docs, prompt files, fakeable LLM
  boundaries, fixture-backed tests, `pyproject.toml` dev tooling, and local
  verification commands.
- Copied-project CI stays intentionally small: the required GitHub Actions
  workflow sets up Python, installs `.[dev]`, and runs `make verify`.
- `make verify-full` is the heavier release/review gate. It runs the fast gate
  first, then runs each template's own `make verify` command.
