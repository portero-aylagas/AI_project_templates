# Safe Improvement Workflow

All templates include repo-local instructions for this workflow:

```text
inspect -> characterize -> verify setup -> audit -> backlog -> one patch -> verify
```

## Inspect

Identify entry points, package manager, tests, scripts, configuration, prompts,
schemas, provider boundaries, and unrelated local changes before editing.

## Characterize

Before medium or high-risk changes, capture current behavior with tests, smoke
scripts, golden fixtures, or a repeatable manual checklist.

## Verify Setup

Prefer one local command:

```bash
make verify
```

Normal verification must not require live API keys, network access, or paid
services.

## Audit

Use two user-facing audit families:

- Engineering Audits
- AI System Audits

Select only the audit areas relevant to the project. Findings should name risk,
expected behavior, files likely affected, characterization needs, and
verification.

## One Patch

Apply one small patch at a time. Do not combine refactors, features, dependency
changes, UI work, cleanup, and test infrastructure unless the combination is
strictly necessary for the patch.

## Verify

Run the agreed verification command. If it fails, stop, report the failure, and
identify the smallest next diagnostic step.

