"""Configuration for MCP agent workflows."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for MCP and model calls."""

    provider: str = "fake"
    model: str = "fake-mcp-model"
    mcp_server_url: str = "http://localhost:8001/mcp"
    allowed_tools: tuple[str, ...] = ("search_docs",)
    timeout_seconds: int = 30


def load_settings() -> Settings:
    """Load MCP settings from environment variables."""
    allowed = os.getenv("MCP_ALLOWED_TOOLS", "search_docs")
    return Settings(
        provider=os.getenv("LLM_PROVIDER", "fake"),
        model=os.getenv("LLM_MODEL", "fake-mcp-model"),
        mcp_server_url=os.getenv("MCP_SERVER_URL", "http://localhost:8001/mcp"),
        allowed_tools=tuple(item.strip() for item in allowed.split(",") if item.strip()),
        timeout_seconds=int(os.getenv("LLM_TIMEOUT_SECONDS", "30")),
    )

