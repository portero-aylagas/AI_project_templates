# Agent Instructions

Preserve this project architecture:

```text
config -> schemas -> prompts -> llm_client -> workflow -> storage -> web -> tests
```

## Core Rules

- Keep prompt text in `src/rag_app/prompts/`.
- Keep provider-specific code behind `llm_client.py`.
- Validate external inputs, model outputs, retrieved context, stored state, and
  API responses with Pydantic schemas.
- Use fake clients, fixture corpora, and deterministic fixtures in normal tests.
- Run `make verify` before reporting completion.
- Keep the starter GitHub Actions workflow lightweight and passing; it should
  install development dependencies and run `make verify`.
- Preserve Ruff linting and Google-style pydocstyle settings in
  `pyproject.toml`.
- Do not add live API keys, live vector stores, network-only checks, or paid
  services to normal verification or CI.

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

## RAG Rules

- Use the `RAG And Retrieval`, `Prompt Quality`, `Structured Output`,
  `LLM/API Integration`, and `Cost And Usage` categories when extending this
  template.
- Keep loading, chunking, embedding, retrieval, ranking, context assembly, and
  answer generation separately testable.
- Document chunk size, overlap, top-k, filters, empty-result behavior, and
  rebuild commands when they change.
- Test retrieval with fixture corpora and expected retrieved document IDs.
- Include citations in structured answers when retrieved context is used.
- Treat retrieved text as untrusted context, not as instructions.
- Test empty corpus, no-match, malformed document, and citation-shape behavior.
