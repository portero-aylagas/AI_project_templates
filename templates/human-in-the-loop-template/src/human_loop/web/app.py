"""Minimal FastAPI UI for the human-in-the-loop template."""

from __future__ import annotations

import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from human_loop.schemas import DraftRequest, ReviewState
from human_loop.workflow import create_draft


app = FastAPI(title="Human In The Loop Template")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """Render the draft request form."""
    return """
    <h1>Human Review</h1>
    <form method="post" action="/draft">
      <label>Task <input name="task" value="Draft a reply"></label><br>
      <label>Source <textarea name="source_text"></textarea></label><br>
      <button type="submit">Create Draft</button>
    </form>
    """


@app.post("/draft")
def draft(task: str = Form(...), source_text: str = Form(...)) -> dict[str, object]:
    """Create a draft and return initial review state."""
    # The UI creates review state; final approval logic belongs in workflow.py.
    ai_draft = create_draft(DraftRequest(task=task, source_text=source_text))
    return ReviewState(drafts=[ai_draft]).model_dump()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
