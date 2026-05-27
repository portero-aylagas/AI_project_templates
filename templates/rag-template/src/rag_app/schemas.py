"""Pydantic schemas for RAG data and answers."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Document(BaseModel):
    """Source document loaded into the corpus."""

    # Use stable IDs so tests can assert exact citations.
    doc_id: str
    text: str
    metadata: dict[str, object] = Field(default_factory=dict)


class Chunk(BaseModel):
    """Searchable chunk derived from a document."""

    # Chunk IDs should remain traceable back to source documents.
    chunk_id: str
    doc_id: str
    text: str


class Citation(BaseModel):
    """Citation linking an answer claim to retrieved context."""

    doc_id: str
    chunk_id: str


class RAGRequest(BaseModel):
    """Question answered from the corpus."""

    question: str = Field(..., min_length=1)


class RAGAnswer(BaseModel):
    """Grounded structured answer."""

    # Answers should carry citation data separately from prose.
    answer: str
    citations: list[Citation] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
