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

## Verify

```bash
make verify
```

