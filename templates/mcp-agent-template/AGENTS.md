# Project Agent Rules

Use the safe improvement workflow:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

Before changing MCP tool behavior, characterize allowlisting, fake tool results,
and failure behavior. Never broaden tool permissions in the same patch as UI,
prompt, dependency, or provider changes.

Normal verification must not require live MCP servers or live API keys. Public
modules, classes, and functions should be typed, clear, and documented with
Google-style docstrings.

