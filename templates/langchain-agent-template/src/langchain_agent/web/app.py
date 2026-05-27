"""Minimal FastAPI UI for the LangChain agent template."""

from __future__ import annotations

import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from langchain_agent.agent import run_agent
from langchain_agent.schemas import AgentRequest


app = FastAPI(title="LangChain Agent Template")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """Render the agent form."""
    return """
    <h1>LangChain Agent</h1>
    <form method="post" action="/run">
      <label>Objective <textarea name="objective"></textarea></label><br>
      <button type="submit">Run</button>
    </form>
    """


@app.post("/run")
def run(objective: str = Form(...)) -> dict[str, object]:
    """Run the agent from form input."""
    # Keep request parsing here and agent behavior in agent.py.
    return run_agent(AgentRequest(objective=objective)).model_dump()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
