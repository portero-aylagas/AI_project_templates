"""Storage helpers for graph state."""

from __future__ import annotations

import json
from pathlib import Path

from langgraph_agent.schemas import GraphResult


def save_result(result: GraphResult, path: Path) -> None:
    """Persist graph result state as JSON."""
    # Persist state and path together so graph runs remain debuggable.
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(result.model_dump_json(indent=2), encoding="utf-8")


def load_result(path: Path) -> GraphResult:
    """Load and validate a persisted graph result."""
    # Treat persisted graph data as external input and validate on load.
    return GraphResult.model_validate(json.loads(path.read_text(encoding="utf-8")))
