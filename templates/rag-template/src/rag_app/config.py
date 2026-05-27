"""Configuration for RAG workflows."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Runtime settings for retrieval and generation."""

    # Defaults keep the copied template offline and deterministic. Replace fake
    # provider/model values only after fixture retrieval tests are stable.
    provider: str = "fake"
    model: str = "fake-rag-model"
    embedding_model: str = "fake-embedding-model"
    # Keep retrieval policy visible; hidden chunking defaults are hard to debug.
    top_k: int = 4
    chunk_size: int = 800
    chunk_overlap: int = 120


def load_settings() -> Settings:
    """Load RAG settings from environment variables."""
    # Centralized parsing keeps workflow functions pure enough for fixture tests.
    return Settings(
        provider=os.getenv("LLM_PROVIDER", "fake"),
        model=os.getenv("LLM_MODEL", "fake-rag-model"),
        embedding_model=os.getenv("EMBEDDING_MODEL", "fake-embedding-model"),
        top_k=int(os.getenv("RAG_TOP_K", "4")),
        chunk_size=int(os.getenv("CHUNK_SIZE", "800")),
        chunk_overlap=int(os.getenv("CHUNK_OVERLAP", "120")),
    )
