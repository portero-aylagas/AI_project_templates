"""Graph workflow tests."""

from langgraph_agent.graph import run_graph
from langgraph_agent.schemas import GraphRequest


def test_graph_records_expected_path_and_status() -> None:
    """The starter graph should run deterministic nodes in order."""
    result = run_graph(GraphRequest(user_goal="Draft a status update"))

    # Path assertions catch accidental node reordering as the graph grows.
    assert result.path == ["classify", "draft", "finalize"]
    assert result.state.status == "complete"
    assert result.state.draft
