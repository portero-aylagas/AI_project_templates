# RAG Template

Use this template for knowledge-base applications that answer questions from a
document corpus. It separates loading, chunking, embedding, retrieval,
reranking, answer generation, citations, and evaluation.

This is not a notebook-style RAG demo. It is a baseline for building auditable
retrieval systems with deterministic fixtures, explicit chunking policy,
structured answers, and documented limitations.

## Quality Intent

- Corpus loading is deterministic.
- Chunk size and overlap are visible configuration.
- Retrieval behavior is tested with fixture documents.
- Answers include structured citations.
- `make verify` is the normal local verification command.

## After Copying

Rename the package and project first, then verify the copied starter before
adding your real corpus or vector store.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
make verify
```

## File Map

- `src/rag_app/config.py`: chunking, retrieval, and model settings.
- `src/rag_app/schemas.py`: document, chunk, citation, request, and answer
  contracts.
- `src/rag_app/workflow.py`: loading, chunking, retrieval, and answer assembly.
- `src/rag_app/prompts/answer.md`: answer-generation instructions.
- `src/rag_app/llm_client.py`: fakeable answer-generation boundary.
- `src/rag_app/web/app.py`: thin demo UI over the workflow.
- `tests/fixtures/`: tiny corpora used to prove retrieval behavior.

## Customize First

Start with representative fixture documents and expected citation behavior.
Then adjust chunk size, overlap, and retrieval logic. Add embeddings or a
vector database only after deterministic fixture tests prove the behavior you
want.

Treat retrieved text as untrusted context. Keep answer schemas and citations
structured so downstream code does not depend on fragile prose.

## Verify

```bash
make verify
```
