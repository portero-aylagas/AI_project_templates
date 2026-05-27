"""Workflow for safe MCP tool execution."""

from __future__ import annotations

from pathlib import Path

from mcp_agent.config import Settings, load_settings
from mcp_agent.llm_client import FakeMCPLLMClient, MCPLLMClient
from mcp_agent.mcp.client import FakeMCPClient, MCPClient
from mcp_agent.schemas import MCPAnswer, MCPRequest


PROMPT_PATH = Path(__file__).parent / "prompts" / "mcp_answer.md"


def run_mcp_workflow(
    request: MCPRequest,
    mcp_client: MCPClient | None = None,
    llm_client: MCPLLMClient | None = None,
    settings: Settings | None = None,
) -> MCPAnswer:
    """Run a safe MCP workflow with tool allowlisting."""
    active_settings = settings or load_settings()
    active_mcp = mcp_client or FakeMCPClient()
    active_llm = llm_client or FakeMCPLLMClient()
    _ = PROMPT_PATH.read_text(encoding="utf-8")

    if request.requested_tool not in active_settings.allowed_tools:
        return MCPAnswer(
            answer="Tool execution blocked.",
            blocked_reason=f"Tool not allowlisted: {request.requested_tool}",
        )

    result = active_mcp.call_tool(
        request.requested_tool,
        {"question": request.question},
    )
    return active_llm.answer(request, result)

