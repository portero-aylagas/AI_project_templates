# How To Use A Template

This repository is a library of starter projects. The normal workflow is to
copy one template into a new repository, rename it, and then build your product
from the existing boundaries instead of starting from an empty folder.

## 1. Choose The Closest Template

Pick the smallest template that matches the first real workflow:

- `simple-llm-call-template`: one direct model call for extraction,
  classification, rewriting, summarization, or report generation.
- `rag-template`: question answering over documents with retrieval and
  citations.
- `langchain-agent-template`: a tool-using agent where LangChain's tool
  abstractions are useful.
- `langgraph-agent-template`: a stateful workflow with explicit graph state and
  node transitions.
- `mcp-agent-template`: an app that calls MCP tools behind an allowlist.
- `human-in-the-loop-template`: AI drafts that must be approved, edited, or
  rejected by a person.

## 2. Copy It Into A New Project

Copy the template folder, then work in the copy:

```bash
cp -R templates/simple-llm-call-template ../my-new-ai-project
cd ../my-new-ai-project
```

After copying, rename the project and package names in:

- `pyproject.toml`
- `src/<package_name>/`
- imports under `src/` and `tests/`
- `README.md` and project docs

## 3. Install And Verify

Create a virtual environment and install development dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Run the local verification command before changing behavior:

```bash
make verify
```

Each copied project includes `.github/workflows/verify.yml`, a small GitHub
Actions workflow that installs development dependencies and runs `make verify`
on push, pull request, and manual dispatch.

The templates use fake clients by default, so normal verification should not
need live API keys, network access, or paid services.

## 4. Build In The Existing Boundaries

Keep the template spine intact while the project is young:

```text
config -> schemas -> prompts -> llm_client -> workflow/agent/graph -> storage -> web -> tests
```

Use each boundary for its intended job:

- `config.py`: environment-driven settings and safe local defaults.
- `schemas.py`: Pydantic contracts for inputs, outputs, tool data, and state.
- `prompts/`: named prompt files that reviewers can inspect.
- `llm_client.py`: the provider boundary; add real clients here, not in
  workflow code.
- `workflow.py`, `agent.py`, or `graph.py`: orchestration and business flow.
- `storage.py`: simple persistence helpers that validate data on load.
- `web/app.py`: thin FastAPI UI that delegates to the workflow layer.
- `tests/`: fake-client and fixture tests that run without live credentials.

## 5. Replace Fakes Deliberately

The fake clients are not placeholders to delete immediately. They are the
reason the project can be tested offline.

When adding a real provider:

- keep the fake client for tests
- implement the same protocol/interface in `llm_client.py`
- add or update schemas before trusting provider output
- keep live-provider tests separate from normal `make verify` and starter CI
- document any required credentials in `.env.example` and `docs/runbook.md`

The copied template should stay small. Add production infrastructure only when
the project actually needs it.
