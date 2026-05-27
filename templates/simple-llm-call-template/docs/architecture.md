# Architecture

The template follows a direct-call architecture:

```text
web/ -> workflow.py -> prompts/ + llm_client.py -> schemas.py -> storage.py
```

`workflow.py` owns orchestration. `llm_client.py` owns provider interaction and
response parsing. `schemas.py` defines the trusted data shapes. Prompt text is
stored as inspectable files under `prompts/`.

