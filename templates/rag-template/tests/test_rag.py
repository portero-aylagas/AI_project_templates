"""RAG workflow tests."""

from pathlib import Path

from rag_app.schemas import RAGRequest
from rag_app.workflow import answer_question, chunk_documents, load_documents


def test_retrieval_answer_includes_citation() -> None:
    """A matching question should produce at least one citation."""
    # This fixture proves retrieval can be tested without embeddings or a DB.
    fixture = Path("tests/fixtures/doc_quality.txt")
    chunks = chunk_documents(load_documents([fixture]))

    answer = answer_question(RAGRequest(question="Why use Pydantic?"), chunks)

    assert answer.citations
    assert answer.citations[0].doc_id == "doc_quality"


def test_empty_corpus_returns_warning() -> None:
    """Empty retrieval should return a structured warning."""
    answer = answer_question(RAGRequest(question="Nothing matches"), [])

    # Empty context should be explicit so callers can decide how to respond.
    assert "no_context" in answer.warnings
