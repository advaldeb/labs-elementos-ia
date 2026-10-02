"""Bucle de agente minimo, independiente de frameworks."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from genai.tools.registry import ToolResult, execute_tool


class AgentDecision(BaseModel):
    """Decision estructurada que el agente toma en un paso."""

    model_config = ConfigDict(extra="forbid")

    action: Literal["tool", "final"]
    tool_name: str | None = None
    arguments: dict[str, Any] = Field(default_factory=dict)
    final_answer: str | None = None

    @model_validator(mode="after")
    def validate_action_fields(self) -> AgentDecision:
        """Exige argumentos de herramienta o respuesta final segun la accion."""
        if self.action == "tool" and (not self.tool_name or self.final_answer is not None):
            raise ValueError("Una decision tool requiere tool_name y no admite final_answer.")
        if self.action == "final" and (not self.final_answer or self.tool_name is not None):
            raise ValueError("Una decision final requiere final_answer y no admite tool_name.")
        return self


class AgentRun(BaseModel):
    """Traza serializable del bucle y su estado terminal."""

    status: Literal[
        "completed",
        "max_steps",
        "max_tool_calls",
        "invalid_decision",
        "unknown_tool",
        "repeated_call",
    ]
    answer: str | None = None
    steps: list[dict[str, Any]] = Field(default_factory=list)


DecisionFunction = Callable[[str, list[dict[str, Any]]], str]


def run_agent(
    request: str,
    decide: DecisionFunction,
    *,
    max_steps: int = 5,
    max_tool_calls: int = 3,
) -> AgentRun:
    """Ejecuta observe-decide-tool-observe con limites estrictos."""
    if max_steps < 1 or max_tool_calls < 0:
        raise ValueError("max_steps debe ser positivo y max_tool_calls no negativo.")

    observations: list[dict[str, Any]] = []
    steps: list[dict[str, Any]] = []
    calls_seen: set[tuple[str, str]] = set()
    tool_calls = 0

    for step_number in range(1, max_steps + 1):
        raw_decision = decide(request, observations)
        try:
            decision = AgentDecision.model_validate_json(raw_decision)
        except (ValidationError, ValueError) as error:
            steps.append({"step": step_number, "error": type(error).__name__})
            return AgentRun(status="invalid_decision", steps=steps)

        if decision.action == "final":
            steps.append({"step": step_number, "action": "final"})
            return AgentRun(status="completed", answer=decision.final_answer, steps=steps)

        call_key = (decision.tool_name or "", str(sorted(decision.arguments.items())))
        if call_key in calls_seen:
            steps.append({"step": step_number, "tool": decision.tool_name, "error": "llamada_repetida"})
            return AgentRun(status="repeated_call", steps=steps)
        calls_seen.add(call_key)

        if tool_calls >= max_tool_calls:
            steps.append({"step": step_number, "tool": decision.tool_name, "error": "limite_herramientas"})
            return AgentRun(status="max_tool_calls", steps=steps)

        result: ToolResult = execute_tool(decision.tool_name or "", decision.arguments)
        tool_calls += 1
        observation = {
            "tool_name": result.tool_name,
            "success": result.success,
            "output": result.output,
            "error": result.error,
        }
        observations.append(observation)
        steps.append({"step": step_number, "action": "tool", **observation})
        if result.error == "herramienta_desconocida":
            return AgentRun(status="unknown_tool", steps=steps)

    return AgentRun(status="max_steps", steps=steps)