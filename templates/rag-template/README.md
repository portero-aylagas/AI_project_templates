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

## Verify

```bash
make verify
```

