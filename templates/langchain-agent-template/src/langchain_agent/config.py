"""Configuration for LangChain agent workflows."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for agent model calls."""

    # Fake defaults make the copied project testable before a real provider is
    # configured. Keep model settings centralized here instead of in agent code.
    provider: str = "fake"
    model: str = "fake-agent-model"
    temperature: float = 0.0
    timeout_seconds: int = 30
    max_output_tokens: int = 1000


def load_settings() -> Settings:
    """Load settings from environment variables."""
    # Environment parsing belongs here so tests can inject Settings directly.
    return Settings(
        provider=os.getenv("LLM_PROVIDER", "fake"),
        model=os.getenv("LLM_MODEL", "fake-agent-model"),
        temperature=float(os.getenv("LLM_TEMPERATURE", "0")),
        timeout_seconds=int(os.getenv("LLM_TIMEOUT_SECONDS", "30")),
        max_output_tokens=int(os.getenv("LLM_MAX_OUTPUT_TOKENS", "1000")),
    )
