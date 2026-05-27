"""RAG workflow with deterministic loading, chunking, retrieval, and answering."""

from __future__ import annotations

from pathlib import Path

from rag_app.config import Settings, load_settings
from rag_app.llm_client import FakeRAGLLMClient, RAGLLMClient
from rag_app.schemas import Chunk, Document, RAGAnswer, RAGRequest


PROMPT_PATH = Path(__file__).parent / "prompts" / "answer.md"


def load_documents(paths: list[Path]) -> list[Document]:
    """Load documents deterministically from sorted paths."""
    # Sorting keeps fixture order stable across operating systems and CI runs.
    documents: list[Document] = []
    for path in sorted(paths):
        documents.append(Document(doc_id=path.stem, text=path.read_text(encoding="utf-8")))
    return documents


def chunk_documents(documents: list[Document], settings: Settings | None = None) -> list[Chunk]:
    """Create simple deterministic chunks from documents."""
    active_settings = settings or load_settings()
    chunks: list[Chunk] = []
    for document in documents:
        text = document.text
        # The starter chunker is intentionally simple. Replace it behind this
        # function when the copied project needs token-aware chunking.
        step = max(1, active_settings.chunk_size - active_settings.chunk_overlap)
        for index, start in enumerate(range(0, len(text), step)):
            chunk_text = text[start : start + active_settings.chunk_size]
            if chunk_text:
                chunks.append(
                    Chunk(
                        chunk_id=f"{document.doc_id}-{index}",
                        doc_id=document.doc_id,
                        text=chunk_text,
                    )
                )
    return chunks


def retrieve(question: str, chunks: list[Chunk], top_k: int) -> list[Chunk]:
    """Return deterministic keyword matches with clear empty-result behavior."""
    # Keyword matching is easy to test. Swap it for embeddings only after
    # expected document IDs are covered by fixtures.
    terms = {term.lower() for term in question.split() if len(term) > 2}
    matches = [
        chunk
        for chunk in chunks
        if any(term in chunk.text.lower() for term in terms)
    ]
    return matches[:top_k]


def answer_question(
    request: RAGRequest,
    chunks: list[Chunk],
    client: RAGLLMClient | None = None,
    settings: Settings | None = None,
) -> RAGAnswer:
    """Answer a question from already-prepared chunks."""
    active_settings = settings or load_settings()
    # The fake client keeps normal verification offline and citation-aware.
    active_client = client or FakeRAGLLMClient()
    _ = PROMPT_PATH.read_text(encoding="utf-8")
    retrieved = retrieve(request.question, chunks, active_settings.top_k)
    return active_client.answer(request.question, retrieved)
