# Architecture

The template separates the agent from tools and provider calls:

```text
web/ -> agent.py -> tools/ + prompts/ + llm_client.py -> schemas.py -> storage.py
```

Tool contracts live in schemas and tool modules. Agent orchestration validates
tool inputs, records tool calls, and returns a structured final response.

## How To Extend It

Add tools as typed functions with fakeable behavior before connecting live
systems. The agent should record what tool was called, what input was used, and
what structured output came back.

Keep final-answer creation behind `llm_client.py` so tests can assert the tool
trace without requiring live model calls.
