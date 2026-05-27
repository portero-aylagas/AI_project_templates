# Architecture

The template treats MCP as an external tool boundary:

```text
web/ -> workflow.py -> mcp/client.py + prompts/ + llm_client.py -> schemas.py
```

Tools are discovered through the MCP client boundary and filtered through an
allowlist before execution. Tool results are parsed into typed schemas.

## How To Extend It

Add new MCP tools by updating the allowlist, schema expectations, fake MCP
responses, and blocked-tool tests together. A tool should not become callable
just because a live server exposes it.

Keep the MCP client boundary narrow. The workflow should receive typed results,
not raw server payloads.
