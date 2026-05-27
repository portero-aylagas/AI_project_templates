# Template Selection Guide

Choose the simplest template that fits the job.

## Direct Model Call

Use `simple-llm-call-template` when the workflow is one or a few model calls:
summarization, classification, extraction, rewriting, or report generation.

## LangChain Agent

Use `langchain-agent-template` when you need LangChain's agent and tool
abstractions and the model should choose among typed tools.

## LangGraph Workflow

Use `langgraph-agent-template` when workflow state, deterministic routing,
approval points, or repeatable node-level tests matter more than free-form tool
selection.

## MCP Agent

Use `mcp-agent-template` when tools are exposed by MCP servers and must be
discovered, allowlisted, called safely, and tested through fake MCP responses.

## RAG

Use `rag-template` when answers must be grounded in a document corpus with
retrieval, citations, and evaluation against fixture documents.

## Human In The Loop

Use `human-in-the-loop-template` when AI output is a draft or recommendation
that a person must approve, edit, or reject before it becomes final.

