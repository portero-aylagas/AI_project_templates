# Project Agent Rules

Use the safe improvement workflow:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

Before changing code, inspect entry points, prompts, schemas, tests,
configuration, and provider boundaries. Make one focused patch at a time. Do not
combine refactors, feature changes, dependency changes, UI changes, and cleanup.

Normal verification must not require live API keys, network access, or paid
services. Use fake clients and deterministic fixtures for AI/API tests.

Public modules, classes, and functions should be beginner/intermediate-friendly,
typed at public boundaries, and documented with concise Google-style docstrings.

