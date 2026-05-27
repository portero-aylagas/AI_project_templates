# Project Agent Rules

Use the safe improvement workflow:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

Before changing chunking, retrieval, ranking, embeddings, prompt contracts, or
answer schemas, characterize retrieval behavior with fixture documents and
expected document IDs.

Normal verification must not require live vector stores, network access, or live
API keys. Public modules, classes, and functions should be typed, clear, and
documented with Google-style docstrings.

