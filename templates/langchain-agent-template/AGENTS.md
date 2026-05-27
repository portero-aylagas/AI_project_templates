# Project Agent Rules

Use the safe improvement workflow:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

Before changing agent behavior, characterize current tool-call behavior with
fake tools or deterministic fixtures. Do not mix prompt edits, tool-contract
changes, provider changes, and UI changes in one patch.

Normal verification must not require live API keys. Public modules, classes, and
functions should be typed, clear, and documented with Google-style docstrings.

