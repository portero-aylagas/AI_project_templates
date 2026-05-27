# Runbook

## Setup

```bash
python -m pip install -e ".[dev]"
```

Tests use fake MCP clients. Live MCP server configuration belongs in `.env`.

## Verify

```bash
make verify
```

## Development Loop

1. Decide which MCP tool names are allowed.
2. Add typed schemas and fake MCP results.
3. Test allowed, blocked, and failed tool behavior.
4. Connect the live MCP client only after fake tests pass.
5. Run `make verify`.
