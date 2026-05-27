# Human In The Loop Template

Use this template when AI produces drafts or recommendations that a person must
approve, edit, or reject before they become final.

This is a standalone human review system. It keeps AI drafts, human decisions,
run state, and audit logs explicit so the workflow can be inspected and
improved safely.

## Quality Intent

- AI drafts are structured and validated.
- Review actions are persisted as approve, edit, or reject decisions.
- Run state and audit records are separate from generated display output.
- Tests use fake LLM clients and local storage fixtures.
- `make verify` is the normal local verification command.

## After Copying

Rename the package and project, then verify the copied starter before adding
real users, notifications, or external side effects.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
make verify
```

## File Map

- `src/human_loop/config.py`: model and review-storage settings.
- `src/human_loop/schemas.py`: draft, review decision, audit, and state
  contracts.
- `src/human_loop/prompts/draft.md`: draft-generation instructions.
- `src/human_loop/llm_client.py`: fakeable draft-generation boundary.
- `src/human_loop/workflow.py`: draft creation and review transitions.
- `src/human_loop/storage.py`: JSON persistence for review state.
- `tests/`: examples for draft creation and audit-producing decisions.

## Customize First

Start by defining the review states and audit fields your project needs. Keep
approve, edit, and reject as explicit transitions. Add tests for unknown drafts
and persistence before adding real external actions.

Do not let AI output become final automatically when the project affects users,
messages, files, or external systems.

## Verify

```bash
make verify
```
