# Architecture

The template uses explicit graph-style workflow boundaries:

```text
web/ -> graph.py -> node functions -> prompts/ + llm_client.py -> schemas.py
```

State is typed with Pydantic. Nodes return structured updates. Routing rules are
plain functions so they can be tested without running live models.

## How To Extend It

Add or change `GraphState` before changing nodes. Each node should take state,
return updated state, and avoid hidden global mutation.

Keep deterministic routing separate from model calls. That makes path tests
fast and keeps failures easier to isolate.
