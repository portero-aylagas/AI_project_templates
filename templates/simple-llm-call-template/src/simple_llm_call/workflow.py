"""Main workflow for direct LLM calls."""

from __future__ import annotations

from pathlib import Path

from simple_llm_call.config import Settings, load_settings
from simple_llm_call.llm_client import FakeLLMClient, LLMClient
from simple_llm_call.schemas import GenerationRequest, WorkflowResponse


PROMPT_PATH = Path(__file__).parent / "prompts" / "generation.md"


def render_prompt(request: GenerationRequest) -> str:
    """Render the named prompt with explicit user-provided variables."""
    template = PROMPT_PATH.read_text(encoding="utf-8")
    return template.format(task=request.task, input_text=request.input_text)


def run_generation(
    request: GenerationRequest,
    client: LLMClient | None = None,
    settings: Settings | None = None,
) -> WorkflowResponse:
    """Run a direct structured model call."""
    active_settings = settings or load_settings()
    active_client = client or FakeLLMClient()
    result = active_client.generate_structured(render_prompt(request))
    return WorkflowResponse(request=request, result=result, model=active_settings.model)

