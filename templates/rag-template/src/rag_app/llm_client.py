"""Provider boundary for RAG answer generation."""

from __future__ import annotations

from typing import Protocol

from rag_app.schemas import Chunk, Citation, RAGAnswer


# Keep answer generation behind a protocol so retrieval tests do not require a
# live model and live providers can be swapped in later.
class RAGLLMClient(Protocol):
    """Protocol implemented by live and fake RAG model clients."""

    def answer(self, question: str, chunks: list[Chunk]) -> RAGAnswer:
        """Generate a structured answer from retrieved chunks."""


class FakeRAGLLMClient:
    """Deterministic RAG model client for tests."""

    def answer(self, question: str, chunks: list[Chunk]) -> RAGAnswer:
        """Return a stable grounded answer."""
        if not chunks:
            # Empty retrieval is a normal RAG outcome, not an exception.
            return RAGAnswer(answer="No matching context found.", warnings=["no_context"])
        citations = [Citation(doc_id=chunk.doc_id, chunk_id=chunk.chunk_id) for chunk in chunks[:1]]
        return RAGAnswer(answer=f"Answer to '{question}' from fixture context.", citations=citations)
