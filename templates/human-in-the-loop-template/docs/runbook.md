# Runbook

## Setup

```bash
python -m pip install -e ".[dev]"
```

## Verify

```bash
make verify
```

## Review Flow

Create a draft, inspect it in the review UI, then approve, edit, or reject it.
Each decision should create an audit entry.

## Development Loop

1. Define the review state and audit fields.
2. Update draft and decision schemas.
3. Test approve, edit, reject, and unknown draft behavior.
4. Add external side effects only after approval is persisted.
5. Run `make verify`.
