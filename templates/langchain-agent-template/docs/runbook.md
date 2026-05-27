# Runbook

## Setup

```bash
python -m pip install -e ".[dev]"
```

Use `.env.example` as a guide for live runs. Tests use fake tools and fake model
clients.

## Verify

```bash
make verify
```

## Development Loop

1. Define or narrow the tool contract.
2. Add a fake tool result for tests.
3. Update the agent prompt and orchestration.
4. Assert the tool trace and structured final answer.
5. Run `make verify`.
