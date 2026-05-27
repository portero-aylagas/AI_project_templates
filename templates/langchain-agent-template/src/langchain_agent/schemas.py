"""Pydantic schemas for agent requests, tools, and responses."""

from __future__ import annotations

from pydantic import BaseModel, Field


class AgentRequest(BaseModel):
    """User request handled by the agent."""

    # Keep the user objective typed before it reaches prompts or tools.
    objective: str = Field(..., min_length=1)


class ToolCall(BaseModel):
    """Trace record for a tool call."""

    # Tool traces make agent behavior reviewable and testable.
    name: str
    input: dict[str, object] = Field(default_factory=dict)
    output: dict[str, object] = Field(default_factory=dict)


class AgentAnswer(BaseModel):
    """Structured final answer returned by the agent."""

    # Return both prose and trace data so callers do not parse free text.
    answer: str
    tool_calls: list[ToolCall] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


class ToolResult(BaseModel):
    """Generic typed result returned by a local tool."""

    # Tools should report success or failure explicitly instead of raising for
    # every expected business condition.
    ok: bool
    data: dict[str, object] = Field(default_factory=dict)
    error: str | None = None
