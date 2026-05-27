# Runbook

## Setup

```bash
python -m pip install -e ".[dev]"
```

## Verify

```bash
make verify
```

## CI

Copied projects include `.github/workflows/verify.yml`, which installs
development dependencies and runs `make verify` on push, pull request, and
manual dispatch. Keep live-provider, paid-service, and network-only checks out
of normal CI.

## Development Notes

Characterize graph paths before changing state schemas, routing, node behavior,
or prompts.

## Development Loop

1. Update `GraphState` for the data the workflow must carry.
2. Add or change one node at a time.
3. Test the path and terminal status.
4. Keep model-backed nodes fakeable.
5. Run `make verify`.
