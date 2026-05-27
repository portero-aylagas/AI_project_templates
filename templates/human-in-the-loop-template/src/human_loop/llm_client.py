"""Provider boundary for AI draft generation."""

from __future__ import annotations

from typing import Protocol

from human_loop.schemas import AIDraft, DraftRequest


# Draft generation depends on this protocol so review tests can use a fake
# client and live provider code can be added later.
class DraftLLMClient(Protocol):
    """Protocol implemented by live and fake draft clients."""

    def create_draft(self, request: DraftRequest) -> AIDraft:
        """Create a structured AI draft."""


class FakeDraftLLMClient:
    """Deterministic draft client for tests."""

    def create_draft(self, request: DraftRequest) -> AIDraft:
        """Return a stable pending draft."""
        # The fake draft is intentionally simple but still uses the real schema.
        return AIDraft(task=request.task, content=f"Draft: {request.source_text}")
