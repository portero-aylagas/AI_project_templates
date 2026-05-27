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

## After Copying

Rename the package and project, then verify the copied starter before
connecting a live MCP server.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
make verify
```

## File Map

- `src/mcp_agent/config.py`: MCP server URL, allowlist, and model settings.
- `src/mcp_agent/schemas.py`: request, tool result, and answer contracts.
- `src/mcp_agent/mcp/client.py`: fakeable MCP client boundary.
- `src/mcp_agent/workflow.py`: allowlist check, tool call, and answer flow.
- `src/mcp_agent/prompts/mcp_answer.md`: answer-generation instructions.
- `src/mcp_agent/llm_client.py`: fakeable model boundary.
- `tests/`: allowed-tool and blocked-tool examples.

## Customize First

Start by deciding which MCP tools are allowed and what their typed results look
like. Add fake MCP responses before wiring live server calls. Keep the allowlist
check in the workflow path so new tools cannot be executed accidentally.

Do not broaden tool execution until tests cover allowed tools, blocked tools,
tool failures, and malformed tool results.

## Verify

```bash
make verify
```
