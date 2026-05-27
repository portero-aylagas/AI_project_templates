"""Typed local tools used by the starter agent."""

from __future__ import annotations

from langchain_agent.schemas import ToolResult


def lookup_policy(topic: str) -> ToolResult:
    """Return a deterministic policy lookup result for a topic."""
    # Starter tools should be boring and typed. Live tools can use the same
    # input/output pattern once tests cover expected behavior.
    if not topic.strip():
        return ToolResult(ok=False, error="topic must not be empty")
    return ToolResult(ok=True, data={"topic": topic, "policy": "Use structured output."})
