# Architecture

The template treats MCP as an external tool boundary:

```text
web/ -> workflow.py -> mcp/client.py + prompts/ + llm_client.py -> schemas.py
```

Tools are discovered through the MCP client boundary and filtered through an
allowlist before execution. Tool results are parsed into typed schemas.

