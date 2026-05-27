"""Workflow tests for the simple LLM call template."""

from simple_llm_call.schemas import GenerationRequest
from simple_llm_call.workflow import render_prompt, run_generation


def test_prompt_rendering_includes_explicit_inputs() -> None:
    """Prompt rendering should include task and input text."""
    request = GenerationRequest(task="Summarize", input_text="Fixture text")

    prompt = render_prompt(request)

    assert "Summarize" in prompt
    assert "Fixture text" in prompt


def test_workflow_returns_structured_output_with_fake_client() -> None:
    """The workflow should return a validated structured response."""
    request = GenerationRequest(task="Summarize", input_text="Fixture text")

    response = run_generation(request)

    assert response.result.title
    assert response.model

