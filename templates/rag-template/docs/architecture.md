# Architecture

The template separates the RAG pipeline:

```text
load -> chunk -> embed -> retrieve -> assemble context -> generate answer
```

Each step is independently testable. Answer generation returns a structured
response with citations so downstream code does not depend on fragile free text.

