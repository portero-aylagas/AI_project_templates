# Architecture

The template follows a direct-call architecture:

```text
web/ -> workflow.py -> prompts/ + llm_client.py -> schemas.py -> storage.py
```

`workflow.py` owns orchestration. `llm_client.py` owns provider interaction and
response parsing. `schemas.py` defines the trusted data shapes. Prompt text is
stored as inspectable files under `prompts/`.

## How To Extend It

When the copied project changes, update the schema first, then the prompt, then
the fake client and workflow tests. This order keeps the contract clear before
any live provider is introduced.

Keep the web layer thin. It should parse form/API input, create a
`GenerationRequest`, call `run_generation`, and return the validated response.
