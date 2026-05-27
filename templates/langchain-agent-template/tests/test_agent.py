"""Agent tests using fake tools and fake clients."""

from langchain_agent.agent import run_agent
from langchain_agent.schemas import AgentRequest


def test_agent_returns_structured_answer_with_tool_trace() -> None:
    """Agent output should include a structured tool trace."""
    answer = run_agent(AgentRequest(objective="Explain structured output"))

    # This is the minimum useful agent test: answer plus inspectable tool trace.
    assert answer.answer
    assert answer.tool_calls[0].name == "lookup_policy"
