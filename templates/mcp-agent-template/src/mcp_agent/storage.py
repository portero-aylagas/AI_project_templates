"""Storage helpers for MCP workflow answers."""

from __future__ import annotations

import json
from pathlib import Path

from mcp_agent.schemas import MCPAnswer


def save_answer(answer: MCPAnswer, path: Path) -> None:
    """Persist an MCP answer as JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(answer.model_dump_json(indent=2), encoding="utf-8")


def load_answer(path: Path) -> MCPAnswer:
    """Load and validate a persisted MCP answer."""
    return MCPAnswer.model_validate(json.loads(path.read_text(encoding="utf-8")))

