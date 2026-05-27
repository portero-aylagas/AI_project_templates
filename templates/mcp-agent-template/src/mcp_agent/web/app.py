"""Minimal FastAPI UI for the MCP agent template."""

from __future__ import annotations

import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from mcp_agent.schemas import MCPRequest
from mcp_agent.workflow import run_mcp_workflow


app = FastAPI(title="MCP Agent Template")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """Render the MCP request form."""
    return """
    <h1>MCP Agent</h1>
    <form method="post" action="/run">
      <label>Question <textarea name="question"></textarea></label><br>
      <label>Tool <input name="requested_tool" value="search_docs"></label><br>
      <button type="submit">Run</button>
    </form>
    """


@app.post("/run")
def run(question: str = Form(...), requested_tool: str = Form("search_docs")) -> dict[str, object]:
    """Run the MCP workflow from form input."""
    return run_mcp_workflow(
        MCPRequest(question=question, requested_tool=requested_tool)
    ).model_dump()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

