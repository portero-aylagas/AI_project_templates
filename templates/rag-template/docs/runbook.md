# Runbook

## Setup

```bash
python -m pip install -e ".[dev]"
```

Place fixture documents under `tests/fixtures/` and runtime documents under
`data/runtime/` in real projects.

## Verify

```bash
make verify
```

## Development Loop

1. Add fixture documents that represent real questions.
2. Write expected citation or empty-result behavior in tests.
3. Tune chunking and retrieval with deterministic fixtures.
4. Add live embeddings or vector stores behind boundaries later.
5. Run `make verify`.
