# Architecture

The template separates the RAG pipeline:

```text
load -> chunk -> embed -> retrieve -> assemble context -> generate answer
```

Each step is independently testable. Answer generation returns a structured
response with citations so downstream code does not depend on fragile free text.

## How To Extend It

Start with fixture documents and expected citations. Then replace one pipeline
piece at a time: chunking, retrieval, ranking, embeddings, or generation.

Keep retrieval tests deterministic. Live embeddings and vector stores should be
added behind boundaries so normal tests can still run offline.
