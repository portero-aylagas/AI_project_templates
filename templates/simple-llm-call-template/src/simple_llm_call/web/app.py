"""Minimal FastAPI UI for the simple LLM call template."""

from __future__ import annotations

import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from simple_llm_call.schemas import GenerationRequest
from simple_llm_call.workflow import run_generation


app = FastAPI(title="Simple LLM Call Template")


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """Render the single-form UI."""
    return """
    <h1>Simple LLM Call</h1>
    <form method="post" action="/generate">
      <label>Task <input name="task" value="Summarize"></label><br>
      <label>Input <textarea name="input_text"></textarea></label><br>
      <button type="submit">Run</button>
    </form>
    """


@app.post("/generate")
def generate(task: str = Form(...), input_text: str = Form(...)) -> dict[str, object]:
    """Run the workflow from form input."""
    response = run_generation(GenerationRequest(task=task, input_text=input_text))
    return response.model_dump()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

