"""Pydantic schemas for graph state and responses."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class GraphRequest(BaseModel):
    """Input used to initialize graph state."""

    user_goal: str = Field(..., min_length=1)


class GraphState(BaseModel):
    """Typed state passed between graph nodes."""

    user_goal: str
    classification: Literal["simple", "needs_review"] | None = None
    draft: str | None = None
    status: Literal["new", "classified", "drafted", "complete"] = "new"
    warnings: list[str] = Field(default_factory=list)


class GraphResult(BaseModel):
    """Final graph result."""

    state: GraphState
    path: list[str]

