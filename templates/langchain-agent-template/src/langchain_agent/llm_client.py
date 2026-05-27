"""Provider boundary for agent final-answer generation."""

from __future__ import annotations

from typing import Protocol

from langchain_agent.schemas import AgentAnswer, ToolCall


# The agent depends on this protocol, not on a provider SDK. That keeps tool
# orchestration testable with a fake model client.
class AgentLLMClient(Protocol):
    """Protocol implemented by live and fake agent model clients."""

    def produce_answer(self, objective: str, tool_calls: list[ToolCall]) -> AgentAnswer:
        """Produce a validated final answer from the objective and tool trace."""


class FakeAgentLLMClient:
    """Deterministic fake agent model client."""

    def produce_answer(self, objective: str, tool_calls: list[ToolCall]) -> AgentAnswer:
        """Return a stable structured answer for tests."""
        # Echo the tool trace so tests can prove the agent called expected tools.
        return AgentAnswer(
            answer=f"Completed objective with {len(tool_calls)} tool call(s): {objective}",
            tool_calls=tool_calls,
        )
