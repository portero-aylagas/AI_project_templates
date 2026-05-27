"""Storage helpers for RAG answers."""

from __future__ import annotations

import json
from pathlib import Path

from rag_app.schemas import RAGAnswer


def save_answer(answer: RAGAnswer, path: Path) -> None:
    """Persist a RAG answer as JSON."""
    # Persist the structured answer, including citations and warnings.
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(answer.model_dump_json(indent=2), encoding="utf-8")


def load_answer(path: Path) -> RAGAnswer:
    """Load and validate a persisted RAG answer."""
    # Saved JSON is external input; validate it before using it again.
    return RAGAnswer.model_validate(json.loads(path.read_text(encoding="utf-8")))
