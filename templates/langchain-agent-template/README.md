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

## Verify

```bash
make verify
```

