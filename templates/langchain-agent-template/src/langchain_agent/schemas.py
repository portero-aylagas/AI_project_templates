"""Pydantic schemas for agent requests, tools, and responses."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """User request handled by the agent."""

    objective: str = Field(..., min_length=1)


class ToolCall(BaseModel):
    """Trace record for a tool call."""

    name: str
    input: dict[str, object] = Field(default_factory=dict)
    output: dict[str, object] = Field(default_factory=dict)


class AgentAnswer(BaseModel):
    """Structured final answer returned by the agent."""

    answer: str
    tool_calls: list[ToolCall] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class ToolResult(BaseModel):
    """Generic typed result returned by a local tool."""

    ok: bool
    data: dict[str, object] = Field(default_factory=dict)
    error: str | None = None

