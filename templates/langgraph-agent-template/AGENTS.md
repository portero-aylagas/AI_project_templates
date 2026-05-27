# Project Agent Rules

Use the safe improvement workflow:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

Before changing graph routing, state schemas, prompts, or provider adapters,
characterize existing graph behavior with deterministic tests. Keep node logic,
model calls, storage, and UI separated.

Normal verification must not require live API keys. Public modules, classes, and
functions should be typed, clear, and documented with Google-style docstrings.

