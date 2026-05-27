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

## Verify

```bash
make verify
```

