# MCP Agent Template

Use this template for AI applications that call tools exposed by MCP servers.
The template focuses on safe discovery, explicit allowlisting, typed tool
payloads, fake MCP tests, and structured model outputs.

This is not an unrestricted tool-calling demo. MCP tools are treated as an
external boundary that needs validation, logging, and clear failure behavior.

## Quality Intent

- Tool names are allowlisted before execution.
- MCP tool results are parsed into Pydantic schemas.
- Tests use fake MCP clients and do not require live servers.
- Logs include run IDs but not secrets or sensitive payloads.
- `make verify` is the normal local verification command.

## Verify

```bash
make verify
```

