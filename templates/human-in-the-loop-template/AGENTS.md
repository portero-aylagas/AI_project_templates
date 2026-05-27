# Project Agent Rules

Use the safe improvement workflow:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

Before changing review state, approval behavior, schemas, prompts, or storage,
characterize approve, edit, reject, and audit-log behavior with deterministic
fixtures.

Normal verification must not require live API keys. Public modules, classes, and
functions should be typed, clear, and documented with Google-style docstrings.

