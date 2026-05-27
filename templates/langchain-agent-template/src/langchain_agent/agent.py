"""Agent orchestration boundary."""

from __future__ import annotations

from pathlib import Path

from langchain_agent.config import Settings, load_settings
from langchain_agent.llm_client import AgentLLMClient, FakeAgentLLMClient
from langchain_agent.schemas import AgentRequest, AgentAnswer, ToolCall
from langchain_agent.tools.catalog import lookup_policy


PROMPT_PATH = Path(__file__).parent / "prompts" / "agent_instructions.md"


def load_agent_instructions() -> str:
    """Load inspectable agent instructions."""
    return PROMPT_PATH.read_text(encoding="utf-8")


def run_agent(
    request: AgentRequest,
    client: AgentLLMClient | None = None,
    settings: Settings | None = None,
) -> AgentAnswer:
    """Run the starter tool agent with deterministic tool wiring."""
    _ = settings or load_settings()
    _ = load_agent_instructions()
    active_client = client or FakeAgentLLMClient()
    tool_result = lookup_policy(request.objective)
    tool_call = ToolCall(
        name="lookup_policy",
        input={"topic": request.objective},
        output=tool_result.model_dump(),
    )
    return active_client.produce_answer(request.objective, [tool_call])

