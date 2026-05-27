# LangChain Agent Template

Use this template when a model should choose among typed tools and LangChain's
agent/tool abstractions are useful.

This is not a chatbot demo. It is a maintainable agent baseline with explicit
tool contracts, fake tools for tests, structured final answers, provider
configuration, and documented safety boundaries.

## Quality Intent

- Tools have typed inputs, typed outputs, useful descriptions, and failure
  behavior.
- The final answer is validated with Pydantic.
- Prompt and tool wiring are separated from business logic.
- Tests use fake tools and fake model clients.
- `make verify` is the normal local verification command.

## After Copying

Rename the package and project, then verify the copied starter before replacing
the fake tool or model client.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
make verify
```

## File Map

- `src/langchain_agent/config.py`: model settings with fake-safe defaults.
- `src/langchain_agent/schemas.py`: user request, tool trace, and final answer
  contracts.
- `src/langchain_agent/tools/`: typed tool implementations and fake-friendly
  examples.
- `src/langchain_agent/prompts/agent_instructions.md`: inspectable agent
  instructions.
- `src/langchain_agent/llm_client.py`: fakeable final-answer boundary.
- `src/langchain_agent/agent.py`: deterministic starter orchestration.
- `tests/`: fake-client tests for tool calls and final answer shape.

## Customize First

Start by defining the real tool contracts and their fake equivalents. Keep each
tool narrow, typed, and testable before letting a model choose it. Add live
tools only after the fake tool path has tests for success and failure behavior.

Prefer the simple LLM template when the model does not need to choose tools.

## Verify

```bash
make verify
```
