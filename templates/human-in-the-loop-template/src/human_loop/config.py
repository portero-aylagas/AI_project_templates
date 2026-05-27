"""Configuration for human review workflows."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    """Runtime settings for draft generation and review storage."""

    # Fake defaults keep draft-generation tests offline and repeatable.
    provider: str = "fake"
    model: str = "fake-review-model"
    # Local JSON storage is intentionally simple for copied starter projects.
    storage_path: Path = Path("data/runtime/reviews.json")
    timeout_seconds: int = 30


def load_settings() -> Settings:
    """Load review workflow settings from environment variables."""
    # Centralizing settings keeps review workflow functions easy to test.
    return Settings(
        provider=os.getenv("LLM_PROVIDER", "fake"),
        model=os.getenv("LLM_MODEL", "fake-review-model"),
        storage_path=Path(os.getenv("REVIEW_STORAGE_PATH", "data/runtime/reviews.json")),
        timeout_seconds=int(os.getenv("LLM_TIMEOUT_SECONDS", "30")),
    )
