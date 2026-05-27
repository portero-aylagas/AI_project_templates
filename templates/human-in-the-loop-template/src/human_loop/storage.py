"""Storage helpers for review state."""

from __future__ import annotations

import json
from pathlib import Path

from human_loop.schemas import ReviewState


def save_state(state: ReviewState, path: Path) -> None:
    """Persist review state as JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(state.model_dump_json(indent=2), encoding="utf-8")


def load_state(path: Path) -> ReviewState:
    """Load and validate review state."""
    if not path.exists():
        return ReviewState()
    return ReviewState.model_validate(json.loads(path.read_text(encoding="utf-8")))

