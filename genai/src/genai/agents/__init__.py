"""Bucles de agente y flujos de control."""

from importlib import import_module
from typing import Any

_EXPORTS = {
	"AgentDecision": ("genai.agents.manual", "AgentDecision"),
	"AgentRun": ("genai.agents.manual", "AgentRun"),
	"run_agent": ("genai.agents.manual", "run_agent"),
	"WorkflowResponse": ("genai.agents.graph", "WorkflowResponse"),
	"build_workflow": ("genai.agents.graph", "build_workflow"),
	"AgenticRagResponse": ("genai.agents.agentic_rag", "AgenticRagResponse"),
	"build_agentic_rag": ("genai.agents.agentic_rag", "build_agentic_rag"),
	"run_agentic_rag": ("genai.agents.agentic_rag", "run_agentic_rag"),
}

__all__ = list(_EXPORTS)


def __getattr__(name: str) -> Any:
	if name not in _EXPORTS:
		raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
	module_name, attribute_name = _EXPORTS[name]
	value = getattr(import_module(module_name), attribute_name)
	globals()[name] = value
	return value