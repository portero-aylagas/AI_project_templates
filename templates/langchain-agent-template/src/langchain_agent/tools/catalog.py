"""Typed local tools used by the starter agent."""

from __future__ import annotations

from langchain_agent.schemas import ToolResult


def lookup_policy(topic: str) -> ToolResult:
    """Return a deterministic policy lookup result for a topic."""
    if not topic.strip():
        return ToolResult(ok=False, error="topic must not be empty")
    return ToolResult(ok=True, data={"topic": topic, "policy": "Use structured output."})

