# Architecture

The template separates AI drafting from human decisions:

```text
web/ -> workflow.py -> llm_client.py + prompts/ -> schemas.py -> storage.py
```

AI drafts, review actions, run state, and audit entries are typed separately.
Generated display output is derived from persisted state, not treated as the
source of truth.

