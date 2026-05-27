"""Pydantic schemas for MCP tool workflows."""

from __future__ import annotations

from pydantic import BaseModel, Field


class MCPRequest(BaseModel):
    """User request that may require an MCP tool."""

    # The requested tool is explicit so the workflow can allow or block it.
    question: str = Field(..., min_length=1)
    requested_tool: str = "search_docs"


class MCPToolResult(BaseModel):
    """Validated MCP tool result."""

    # Tool output is typed before it is passed to the model.
    tool_name: str
    ok: bool
    content: str
    metadata: dict[str, object] = Field(default_factory=dict)


class MCPAnswer(BaseModel):
    """Structured answer returned by the MCP workflow."""

    # Blocked tools are represented as data, not silent failures.
    answer: str
    tool_result: MCPToolResult | None = None
    blocked_reason: str | None = None
    warnings: list[str] = Field(default_factory=list)
