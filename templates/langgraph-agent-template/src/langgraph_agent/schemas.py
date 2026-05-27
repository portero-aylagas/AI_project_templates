"""Pydantic schemas for graph state and responses."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class GraphRequest(BaseModel):
    """Input used to initialize graph state."""

    # Validate the initial user goal before creating graph state.
    user_goal: str = Field(..., min_length=1)


class GraphState(BaseModel):
    """Typed state passed between graph nodes."""

    # Keep all cross-node data explicit here. Avoid hidden module globals.
    user_goal: str
    classification: Literal["simple", "needs_review"] | None = None
    draft: str | None = None
    status: Literal["new", "classified", "drafted", "complete"] = "new"
    warnings: list[str] = Field(default_factory=list)


class GraphResult(BaseModel):
    """Final graph result."""

    # Include the path so tests and reviewers can see which nodes ran.
    state: GraphState
    path: list[str]
