"""Storage helpers for workflow outputs."""

from __future__ import annotations

import json
from pathlib import Path

from simple_llm_call.schemas import WorkflowResponse


def save_response(response: WorkflowResponse, path: Path) -> None:
    """Persist a validated workflow response as JSON."""
    # Storage receives already-validated data; validation happens again on load.
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(response.model_dump_json(indent=2), encoding="utf-8")


def load_response(path: Path) -> WorkflowResponse:
    """Load and validate a persisted workflow response."""
    data = json.loads(path.read_text(encoding="utf-8"))
    # Treat saved JSON as external input. Validate it before returning it.
    return WorkflowResponse.model_validate(data)
