"""Graph-style workflow orchestration."""

from __future__ import annotations

from pathlib import Path

from langgraph_agent.config import Settings, load_settings
from langgraph_agent.llm_client import FakeGraphLLMClient, GraphLLMClient
from langgraph_agent.schemas import GraphRequest, GraphResult, GraphState


PROMPT_PATH = Path(__file__).parent / "prompts" / "draft.md"


def classify_node(state: GraphState) -> GraphState:
    """Classify the request using deterministic business rules."""
    # Deterministic rules belong outside the model so routing is testable.
    classification = "needs_review" if "approve" in state.user_goal.lower() else "simple"
    return state.model_copy(
        update={"classification": classification, "status": "classified"}
    )


def draft_node(state: GraphState, client: GraphLLMClient) -> GraphState:
    """Create a model-backed draft and update graph state."""
    # Prompt loading happens here to make the model-backed node explicit.
    _ = PROMPT_PATH.read_text(encoding="utf-8")
    return state.model_copy(update={"draft": client.draft(state.user_goal), "status": "drafted"})


def finalize_node(state: GraphState) -> GraphState:
    """Mark the graph as complete."""
    return state.model_copy(update={"status": "complete"})


def run_graph(
    request: GraphRequest,
    client: GraphLLMClient | None = None,
    settings: Settings | None = None,
) -> GraphResult:
    """Run the starter graph with explicit state transitions."""
    _ = settings or load_settings()
    # Default fake client keeps graph tests offline; inject a live client later.
    active_client = client or FakeGraphLLMClient()
    path: list[str] = []
    state = GraphState(user_goal=request.user_goal)

    # Keep node order visible in the starter. A real graph runtime can replace
    # this once paths, state, and tests are clear.
    state = classify_node(state)
    path.append("classify")
    state = draft_node(state, active_client)
    path.append("draft")
    state = finalize_node(state)
    path.append("finalize")

    return GraphResult(state=state, path=path)
