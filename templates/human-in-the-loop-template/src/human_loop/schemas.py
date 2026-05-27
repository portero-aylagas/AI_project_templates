"""Pydantic schemas for human-in-the-loop review workflows."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Literal
from uuid import uuid4

from pydantic import BaseModel, Field


class DraftRequest(BaseModel):
    """Request used to generate an AI draft."""

    task: str = Field(..., min_length=1)
    source_text: str = Field(..., min_length=1)


class AIDraft(BaseModel):
    """Structured AI draft awaiting human review."""

    draft_id: str = Field(default_factory=lambda: str(uuid4()))
    task: str
    content: str
    status: Literal["pending", "approved", "edited", "rejected"] = "pending"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReviewDecision(BaseModel):
    """Human decision applied to an AI draft."""

    draft_id: str
    action: Literal["approve", "edit", "reject"]
    edited_content: str | None = None
    reviewer_note: str | None = None


class AuditEntry(BaseModel):
    """Audit record for a human review action."""

    draft_id: str
    action: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    note: str | None = None


class ReviewState(BaseModel):
    """Persisted review state."""

    drafts: list[AIDraft] = Field(default_factory=list)
    audit_log: list[AuditEntry] = Field(default_factory=list)

