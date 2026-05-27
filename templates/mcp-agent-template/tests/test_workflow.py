"""MCP workflow tests."""

from mcp_agent.config import Settings
from mcp_agent.schemas import MCPRequest
from mcp_agent.workflow import run_mcp_workflow


def test_allowed_tool_returns_structured_answer() -> None:
    """Allowlisted MCP tools should be executed through the boundary."""
    answer = run_mcp_workflow(MCPRequest(question="What is allowed?"))

    # The fake MCP client proves the boundary without a live server.
    assert answer.tool_result is not None
    assert answer.tool_result.ok


def test_blocked_tool_does_not_execute() -> None:
    """Non-allowlisted tools should be blocked before execution."""
    settings = Settings(allowed_tools=("search_docs",))
    answer = run_mcp_workflow(
        MCPRequest(question="Run a tool", requested_tool="shell"),
        settings=settings,
    )

    # A blocked tool should be explicit and should not return tool_result data.
    assert answer.blocked_reason == "Tool not allowlisted: shell"
