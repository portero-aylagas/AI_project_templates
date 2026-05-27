"""Small MCP client boundary used by the workflow."""

from __future__ import annotations

from typing import Protocol

from mcp_agent.schemas import MCPToolResult


# The workflow talks to this protocol instead of a server SDK. That keeps
# allowed/blocked tool behavior testable with FakeMCPClient.
class MCPClient(Protocol):
    """Protocol implemented by live and fake MCP clients."""

    def call_tool(self, tool_name: str, arguments: dict[str, object]) -> MCPToolResult:
        """Call an MCP tool and return a validated result."""


class FakeMCPClient:
    """Deterministic fake MCP client."""

    def call_tool(self, tool_name: str, arguments: dict[str, object]) -> MCPToolResult:
        """Return a stable fake MCP result."""
        # Echoing the question keeps tests deterministic while preserving shape.
        question = str(arguments.get("question", ""))
        return MCPToolResult(
            tool_name=tool_name,
            ok=True,
            content=f"Fake MCP result for: {question}",
            metadata={"source": "fake-mcp"},
        )
