"""Minimal FastAPI UI for the LangGraph workflow template."""

from __future__ import annotations

import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from langgraph_agent.graph import run_graph
from langgraph_agent.schemas import GraphRequest


app = FastAPI(title="LangGraph Agent Template")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """Render the graph form."""
    return """
    <h1>LangGraph Workflow</h1>
    <form method="post" action="/run">
      <label>Goal <textarea name="user_goal"></textarea></label><br>
      <button type="submit">Run</button>
    </form>
    """


@app.post("/run")
def run(user_goal: str = Form(...)) -> dict[str, object]:
    """Run the graph from form input."""
    return run_graph(GraphRequest(user_goal=user_goal)).model_dump()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

