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

## CI

Copied projects include `.github/workflows/verify.yml`, which installs
development dependencies and runs `make verify` on push, pull request, and
manual dispatch. Keep live-provider, paid-service, and network-only checks out
of normal CI.

## Development Loop

1. Add fixture documents that represent real questions.
2. Write expected citation or empty-result behavior in tests.
3. Tune chunking and retrieval with deterministic fixtures.
4. Add live embeddings or vector stores behind boundaries later.
5. Run `make verify`.
