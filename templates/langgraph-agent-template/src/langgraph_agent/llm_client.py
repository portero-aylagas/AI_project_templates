"""Provider boundary for graph node model calls."""

from __future__ import annotations

from typing import Protocol


# Model-backed graph nodes depend on this protocol. Tests can inject a fake
# client while production code can add a live implementation later.
class GraphLLMClient(Protocol):
    """Protocol implemented by live and fake graph model clients."""

    def draft(self, goal: str) -> str:
        """Draft a response for the user goal."""


class FakeGraphLLMClient:
    """Deterministic graph model client for tests."""

    def draft(self, goal: str) -> str:
        """Return a stable draft."""
        return f"Draft for: {goal}"
