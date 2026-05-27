"""Provider boundary for LLM calls."""

from __future__ import annotations

from typing import Protocol

from simple_llm_call.schemas import GenerationResult


class LLMClient(Protocol):
    """Protocol implemented by live and fake LLM clients."""

    def generate_structured(self, prompt: str) -> GenerationResult:
        """Return a validated structured result for a rendered prompt."""


class FakeLLMClient:
    """Deterministic test client that never calls a live provider."""

    def generate_structured(self, prompt: str) -> GenerationResult:
        """Return a stable result for tests and local smoke runs."""
        first_line = prompt.strip().splitlines()[0] if prompt.strip() else "Result"
        return GenerationResult(
            title="Fake structured response",
            body=f"Processed prompt starting with: {first_line}",
            warnings=[],
        )

