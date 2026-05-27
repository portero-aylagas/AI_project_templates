"""Provider boundary for AI draft generation."""

from __future__ import annotations

from typing import Protocol

from human_loop.schemas import AIDraft, DraftRequest


class DraftLLMClient(Protocol):
    """Protocol implemented by live and fake draft clients."""

    def create_draft(self, request: DraftRequest) -> AIDraft:
        """Create a structured AI draft."""


class FakeDraftLLMClient:
    """Deterministic draft client for tests."""

    def create_draft(self, request: DraftRequest) -> AIDraft:
        """Return a stable pending draft."""
        return AIDraft(task=request.task, content=f"Draft: {request.source_text}")

