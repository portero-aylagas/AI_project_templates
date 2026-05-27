"""Human-in-the-loop draft and review workflow."""

from __future__ import annotations

from pathlib import Path

from human_loop.llm_client import DraftLLMClient, FakeDraftLLMClient
from human_loop.schemas import AIDraft, AuditEntry, DraftRequest, ReviewDecision, ReviewState


PROMPT_PATH = Path(__file__).parent / "prompts" / "draft.md"


def create_draft(
    request: DraftRequest,
    client: DraftLLMClient | None = None,
) -> AIDraft:
    """Create a structured draft for human review."""
    _ = PROMPT_PATH.read_text(encoding="utf-8")
    active_client = client or FakeDraftLLMClient()
    return active_client.create_draft(request)


def apply_decision(state: ReviewState, decision: ReviewDecision) -> ReviewState:
    """Apply a human decision and append an audit entry."""
    updated_drafts: list[AIDraft] = []
    matched = False
    for draft in state.drafts:
        if draft.draft_id != decision.draft_id:
            updated_drafts.append(draft)
            continue

        matched = True
        if decision.action == "approve":
            updated_drafts.append(draft.model_copy(update={"status": "approved"}))
        elif decision.action == "edit":
            content = decision.edited_content or draft.content
            updated_drafts.append(
                draft.model_copy(update={"status": "edited", "content": content})
            )
        else:
            updated_drafts.append(draft.model_copy(update={"status": "rejected"}))

    if not matched:
        raise ValueError(f"Unknown draft_id: {decision.draft_id}")

    audit_entry = AuditEntry(
        draft_id=decision.draft_id,
        action=decision.action,
        note=decision.reviewer_note,
    )
    return ReviewState(
        drafts=updated_drafts,
        audit_log=[*state.audit_log, audit_entry],
    )

