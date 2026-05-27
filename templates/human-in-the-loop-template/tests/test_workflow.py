"""Human-in-the-loop workflow tests."""

from human_loop.schemas import DraftRequest, ReviewDecision, ReviewState
from human_loop.workflow import apply_decision, create_draft


def test_create_draft_returns_pending_structured_draft() -> None:
    """Draft generation should create pending review state data."""
    draft = create_draft(
        DraftRequest(task="Draft a response", source_text="Need a status update.")
    )

    assert draft.status == "pending"
    assert draft.content


def test_apply_approve_decision_updates_state_and_audit_log() -> None:
    """Approving a draft should update status and append an audit entry."""
    draft = create_draft(
        DraftRequest(task="Draft a response", source_text="Need a status update.")
    )
    state = ReviewState(drafts=[draft])

    updated = apply_decision(
        state,
        ReviewDecision(draft_id=draft.draft_id, action="approve"),
    )

    assert updated.drafts[0].status == "approved"
    assert updated.audit_log[0].action == "approve"

