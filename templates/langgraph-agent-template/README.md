# LangGraph Agent Template

Use this template for stateful agent workflows where explicit graph nodes,
conditional routing, state updates, and checkpoint-ready design matter.

The template emphasizes deterministic workflow structure over free-form agent
behavior. Each node has a clear responsibility, typed state, fake-client tests,
and documented failure paths.

## Quality Intent

- Graph state is modeled with Pydantic.
- Nodes return structured state updates.
- Business rules are separated from model calls.
- Tests cover routing and state transitions without live keys.
- `make verify` is the normal local verification command.

## After Copying

Rename the project and package, then run verification before adding new nodes
or persistence.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
make verify
```

## File Map

- `src/langgraph_agent/config.py`: model settings with fake-safe defaults.
- `src/langgraph_agent/schemas.py`: graph request, state, and result contracts.
- `src/langgraph_agent/graph.py`: node functions and transition order.
- `src/langgraph_agent/prompts/draft.md`: model-backed node instructions.
- `src/langgraph_agent/llm_client.py`: fakeable model boundary for graph
  nodes.
- `src/langgraph_agent/storage.py`: JSON persistence for graph results.
- `tests/`: state-transition tests that run without live credentials.

## Customize First

Start by shaping `GraphState` and writing tests for the paths the workflow must
support. Add nodes as small functions with one responsibility. Keep deterministic
routing rules separate from model-backed node calls so failures are easier to
test.

Add checkpointing or a real LangGraph runtime only after the starter state
transitions are clear.

## Verify

```bash
make verify
```
