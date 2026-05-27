"""Storage helpers for agent outputs."""

from __future__ import annotations

import json
from pathlib import Path

from langchain_agent.schemas import AgentAnswer


def save_answer(answer: AgentAnswer, path: Path) -> None:
    """Persist a validated agent answer as JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(answer.model_dump_json(indent=2), encoding="utf-8")


def load_answer(path: Path) -> AgentAnswer:
    """Load and validate a persisted agent answer."""
    return AgentAnswer.model_validate(json.loads(path.read_text(encoding="utf-8")))

