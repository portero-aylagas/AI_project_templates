# AI Project Templates

This repository contains reusable starter architectures for software that
integrates AI. These templates are intentionally not quick demos. They are
designed to make good engineering habits the default before a project grows:
separated prompts, typed schemas, provider boundaries, fake-client tests,
documented limitations, and repeatable verification.

## Templates

| Template | Use it for |
| --- | --- |
| `templates/simple-llm-call-template` | Direct LLM calls for generation, classification, extraction, rewriting, or summarization. |
| `templates/langchain-agent-template` | Tool-using agents where LangChain's tool and agent abstractions are useful. |
| `templates/langgraph-agent-template` | Stateful agent workflows with explicit graph nodes, routing, and checkpoint-ready state. |
| `templates/mcp-agent-template` | Applications that discover and call MCP tools behind a safe allowlist. |
| `templates/rag-template` | Knowledge-base apps with ingestion, chunking, retrieval, citations, and grounded answers. |
| `templates/human-in-the-loop-template` | Review and approval workflows where AI drafts must be accepted, edited, or rejected by a person. |

## Shared Intent

Every template follows the same spine:

```text
config -> schemas -> prompts -> llm_client -> workflow/agent/graph -> storage -> web -> tests
```

The goal is consistency. A project built from any template should be easy to
inspect, test without live keys, extend safely, and review for both software
engineering quality and AI-system quality.

## Quality Defaults

- Prompts live in named files under `src/<package>/prompts/`.
- Pydantic schemas define inputs, outputs, errors, tool payloads, and state.
- External model calls live behind `llm_client.py` or an equivalent adapter.
- Normal tests use fake clients, fake tools, and deterministic fixtures.
- `make verify` is the standard local verification command.
- Each boilerplate includes project-local `AGENTS.md` guidance for future agent
  maintenance after the project is copied.
- FastAPI plus simple HTML is the default UI layer.
- Docs explain architecture, setup, verification, known limitations, trust
  boundaries, and evaluation.

## Repository Verification

Run this from the repository root:

```bash
make verify
```

Root verification checks that every template contains the required quality
artifacts. Each template also has its own `make verify` command for local
development after installing that template's dependencies.
