# Project Spec

## Goal

Provide a reusable baseline for one-step or short-chain LLM features with typed
inputs, structured outputs, fake-client tests, and a minimal FastAPI UI.

## In Scope

- Prompt rendering from named files.
- Direct model calls through a provider boundary.
- Pydantic validation for request and response data.
- Local verification without live credentials.

## Out Of Scope

- Agentic tool choice.
- RAG retrieval.
- Human approval queues.

