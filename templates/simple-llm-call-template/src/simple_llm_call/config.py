"""Configuration for direct LLM call workflows."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for model calls and verification-safe defaults."""

    provider: str = "fake"
    model: str = "fake-structured-model"
    temperature: float = 0.0
    timeout_seconds: int = 30
    max_output_tokens: int = 800


def load_settings() -> Settings:
    """Load settings from environment variables."""
    return Settings(
        provider=os.getenv("LLM_PROVIDER", "fake"),
        model=os.getenv("LLM_MODEL", "fake-structured-model"),
        temperature=float(os.getenv("LLM_TEMPERATURE", "0")),
        timeout_seconds=int(os.getenv("LLM_TIMEOUT_SECONDS", "30")),
        max_output_tokens=int(os.getenv("LLM_MAX_OUTPUT_TOKENS", "800")),
    )

