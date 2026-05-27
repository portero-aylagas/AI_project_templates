# Architecture

The template separates AI drafting from human decisions:

```text
web/ -> workflow.py -> llm_client.py + prompts/ -> schemas.py -> storage.py
```

AI drafts, review actions, run state, and audit entries are typed separately.
Generated display output is derived from persisted state, not treated as the
source of truth.

## How To Extend It

Start by extending the review state and audit schemas. Then update the workflow
tests for every state transition a reviewer can trigger.

Keep external side effects after review approval. Draft generation should create
reviewable state, not perform final actions on its own.
