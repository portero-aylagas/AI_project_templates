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

Use these engineering categories when reviewing or extending a template:

| Category | Template standard |
| --- | --- |
| General Software Architecture | Keep orchestration, business logic, UI, provider calls, storage, configuration, and utilities separated enough to inspect and test independently. |
| Function Responsibility | Keep public functions and classes focused, clearly named, typed at boundaries, and documented with concise Google-style docstrings. |
| Error Handling | Make missing configuration, file failures, bad user input, malformed JSON, and provider failures produce useful messages instead of silent or confusing failures. |
| Testability | Keep workflow logic callable with fake clients, fake tools, fixture data, and local storage so normal tests do not need live services. |
| Data And JSON Validation | Parse user input, uploaded files, API responses, model outputs, tool payloads, retrieved context, and persisted state into typed schemas before downstream use. |
| Repository Hygiene | Keep virtual environments, caches, generated runtime outputs, secrets, and large local artifacts out of copied projects. |
| Documentation And Reviewer Evidence | Document setup, run commands, verification, environment variables, sample inputs, expected outputs, limitations, and fallback behavior. |
| Security And Secrets | Keep credentials out of source control, avoid sensitive logs, validate external boundaries, and treat retrieved/tool/user text as untrusted input. |

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

Use these AI-system categories when reviewing or extending a template:

| Category | Template standard |
| --- | --- |
| AI Software Architecture | Keep provider adapters, prompts, model-call boundaries, deterministic logic, RAG, agents, tools, and workflow components in clear, fakeable modules. |
| Prompt Quality | Keep prompt text named, inspectable, task-specific, explicit about inputs and output format, and covered by focused tests when changed. |
| Dynamic Prompting | Insert variables through one explicit rendering path that separates user or document text from instructions. |
| Structured Output | Validate model, tool, and workflow outputs with schemas before storing, displaying, or passing them downstream. |
| LLM/API Integration | Centralize model names, temperature, timeouts, retries, token limits, credential loading, response parsing, and fake-client support. |
| RAG And Retrieval | Keep loading, chunking, embedding, retrieval, ranking, context assembly, citations, empty-result behavior, and fixture evaluation separately testable. |
| Agents And Tools | Keep tool names, descriptions, inputs, outputs, allowlists, traces, failure behavior, and final-answer extraction explicit and typed. |
| Workflow Automation | Keep state, run IDs, idempotency, retries, failure branches, approval points, logs, recovery notes, and cost controls visible in multi-step flows. |
| Cost And Usage | Make live evaluation, paid services, rate limits, and budget assumptions explicit before adding live-provider checks. |

Speech pipelines are not required in the current templates. If a future template
adds speech-to-text, text-to-speech, or audio processing, it should document
audio loading, chunking, timestamps, generated audio validation, and safe output
naming as a first-class AI-system quality category.

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
