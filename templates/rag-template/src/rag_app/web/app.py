"""Minimal FastAPI UI for the RAG template."""

from __future__ import annotations

import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from rag_app.schemas import Chunk, RAGRequest
from rag_app.workflow import answer_question


app = FastAPI(title="RAG Template")
DEMO_CHUNKS = [Chunk(chunk_id="demo-0", doc_id="demo", text="Templates use Pydantic.")]


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """Render the question form."""
    return """
    <h1>RAG Template</h1>
    <form method="post" action="/ask">
      <label>Question <textarea name="question"></textarea></label><br>
      <button type="submit">Ask</button>
    </form>
    """


@app.post("/ask")
def ask(question: str = Form(...)) -> dict[str, object]:
    """Answer a question from demo chunks."""
    return answer_question(RAGRequest(question=question), DEMO_CHUNKS).model_dump()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

