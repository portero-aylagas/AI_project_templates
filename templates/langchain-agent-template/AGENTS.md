# Agent Instructions

Preserve this project architecture:

```text
config -> schemas -> prompts -> llm_client -> agent -> tools -> storage -> web -> tests
```

## Core Rules

- Keep prompt text in `src/langchain_agent/prompts/`.
- Keep provider-specific code behind `llm_client.py`.
- Validate external inputs, model outputs, tool payloads, stored state, and API
  responses with Pydantic schemas.
- Use fake clients, fake tools, and deterministic fixtures in normal tests.
- Run `make verify` before reporting completion.
- Keep the starter GitHub Actions workflow lightweight and passing; it should
  install development dependencies and run `make verify`.
- Preserve Ruff linting and Google-style pydocstyle settings in
  `pyproject.toml`.
- Do not add live API keys, network-only checks, or paid services to normal
  verification or CI.

## LangChain Agent Rules

- Keep every tool contract typed, documented, and narrow.
- Add or update fake tools before wiring equivalent live tools.
- Test expected tool calls, tool inputs, tool outputs, and final structured
  answers.
- Do not broaden tool access without adding safety and failure tests.
- Keep final-answer extraction explicit and validated before returning it from
  the agent.
- Prefer a direct workflow over an agent when tool choice is not needed.
