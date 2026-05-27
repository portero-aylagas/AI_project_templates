"""Provider boundary for MCP-backed answer generation."""

from __future__ import annotations

from typing import Protocol

from mcp_agent.schemas import MCPAnswer, MCPRequest, MCPToolResult


class MCPLLMClient(Protocol):
    """Protocol implemented by live and fake model clients."""

    def answer(self, request: MCPRequest, result: MCPToolResult | None) -> MCPAnswer:
        """Return a structured answer from a user request and tool result."""


class FakeMCPLLMClient:
    """Deterministic model client for MCP tests."""

    def answer(self, request: MCPRequest, result: MCPToolResult | None) -> MCPAnswer:
        """Return a stable structured MCP answer."""
        if result is None:
            return MCPAnswer(answer="No allowed tool was executed.")
        return MCPAnswer(answer=f"Answered using {result.tool_name}: {result.content}", tool_result=result)

