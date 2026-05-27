# Agent Instructions

Preserve this project architecture:

```text
config -> schemas -> prompts -> llm_client -> mcp/client -> workflow -> storage -> web -> tests
```

## Core Rules

- Keep prompt text in `src/mcp_agent/prompts/`.
- Keep provider-specific code behind `llm_client.py`.
- Validate external inputs, model outputs, MCP tool results, stored state, and
  API responses with Pydantic schemas.
- Use fake clients, fake MCP responses, and deterministic fixtures in normal
  tests.
- Run `make verify` before reporting completion.
- Keep the starter GitHub Actions workflow lightweight and passing; it should
  install development dependencies and run `make verify`.
- Preserve Ruff linting and Google-style pydocstyle settings in
  `pyproject.toml`.
- Do not add live API keys, live MCP servers, network-only checks, or paid
  services to normal verification or CI.

## Shared Quality Rules

- Keep code beginner/intermediate-friendly with clear names, simple control
  flow, and explicit side effects at workflow, MCP, storage, provider, and web
  boundaries.
- Keep public modules, classes, and functions documented with concise
  Google-style docstrings.
- Raise useful error messages for missing configuration, malformed input,
  provider failures, failed tools, and invalid structured output.
- Do not log secrets, credentials, raw sensitive user data, or full provider or
  tool payloads.

## MCP Rules

- Use the `Agents And Tools`, `Workflow Automation`, `Structured Output`,
  `LLM/API Integration`, and `Cost And Usage` categories when extending this
  template.
- Treat MCP tools as untrusted external boundaries.
- Check the tool allowlist before every tool execution.
- Validate MCP tool results before using them in prompts or workflow logic.
- Test allowed tools, blocked tools, failed tools, and malformed tool responses.
- Do not add broad or dynamic tool execution without explicit allowlisting and
  tests.
- Log tool names and run identifiers where useful, but never log secrets or
  sensitive payloads.
