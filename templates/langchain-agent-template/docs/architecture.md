# Architecture

The template separates the agent from tools and provider calls:

```text
web/ -> agent.py -> tools/ + prompts/ + llm_client.py -> schemas.py -> storage.py
```

Tool contracts live in schemas and tool modules. Agent orchestration validates
tool inputs, records tool calls, and returns a structured final response.

