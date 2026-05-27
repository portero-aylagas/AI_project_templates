"""Pydantic schemas for direct LLM call inputs and outputs."""

from __future__ import annotations

from pydantic import BaseModel, Field


class GenerationRequest(BaseModel):
    """User request for a direct model call."""

    task: str = Field(..., min_length=1)
    input_text: str = Field(..., min_length=1)


class GenerationResult(BaseModel):
    """Validated model output trusted by downstream code."""

    title: str
    body: str
    warnings: list[str] = Field(default_factory=list)


class WorkflowResponse(BaseModel):
    """Complete response returned by the workflow."""

    request: GenerationRequest
    result: GenerationResult
    model: str

