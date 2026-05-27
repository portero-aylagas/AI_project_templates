# Architecture

The template uses explicit graph-style workflow boundaries:

```text
web/ -> graph.py -> node functions -> prompts/ + llm_client.py -> schemas.py
```

State is typed with Pydantic. Nodes return structured updates. Routing rules are
plain functions so they can be tested without running live models.

