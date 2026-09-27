"""Workflow LangGraph con rutas RAG, herramientas y respuesta directa."""

from __future__ import annotations

import re
import unicodedata
from typing import Any, Literal, TypedDict

from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, ConfigDict, Field

from llm_engineering.tools.registry import ToolName, ToolResult, execute_tool


class WorkflowResponse(BaseModel):
    """Contrato de salida validada del workflow."""

    model_config = ConfigDict(extra="forbid")

    route: Literal["rag", "tool", "direct"]
    status: Literal["ok", "error"]
    answer: str = Field(min_length=1)
    source_ids: list[str] = Field(default_factory=list)
    tool_result: ToolResult | None = None


class WorkflowState(TypedDict, total=False):
    """Estado compartido por los nodos del grafo."""

    request: str
    route: str
    tool_name: str
    tool_arguments: dict[str, Any]
    raw_output: dict[str, Any]
    validated_output: dict[str, Any]
    validation_error: str | None


def _calculator_expression(request: str) -> str | None:
    """Extrae una operacion aritmetica simple de una solicitud explicita."""
    match = re.search(r"[-+]?\d+(?:\.\d+)?(?:\s*[-+*/]\s*[-+]?\d+(?:\.\d+)?)+", request)
    return match.group(0) if match else None


def _classify_request(state: WorkflowState) -> WorkflowState:
    """Clasifica solicitud para seleccionar una ruta del grafo."""
    request = state["request"]
    if state.get("tool_name"):
        return {"route": "tool"}

    normalized = unicodedata.normalize("NFKD", request)
    normalized = "".join(character for character in normalized if not unicodedata.combining(character))
    normalized = normalized.casefold()
    if any(word in normalized for word in ("calcula", "calcular", "suma", "multiplica")):
        expression = _calculator_expression(request)
        if expression:
            return {
                "route": "tool",
                "tool_name": ToolName.CALCULATOR.value,
                "tool_arguments": {"expression": expression},
            }

    if any(word in normalized for word in (
        "envio", "seguimiento", "devolucion", "reembolso", "paquete",
        "pedido", "pago", "cargo", "politica",
    )):
        return {"route": "rag"}
    return {"route": "direct"}


def _rag_node(state: WorkflowState) -> WorkflowState:
    """Busca evidencia FAQ y la conserva como datos con IDs de origen."""
    result = execute_tool(
        ToolName.DOCUMENT_SEARCH.value,
        {"query": state["request"]},
    )
    return {
        "raw_output": {
            "route": "rag",
            "status": "ok" if result.success else "error",
            "answer": result.output,
            "source_ids": result.source_ids,
            "tool_result": result.model_dump(),
        }
    }


def _tool_node(state: WorkflowState) -> WorkflowState:
    """Valida y ejecuta una herramienta permitida."""
    result = execute_tool(
        state.get("tool_name", ""),
        state.get("tool_arguments", {}),
    )
    return {
        "raw_output": {
            "route": "tool",
            "status": "ok" if result.success else "error",
            "answer": result.output,
            "source_ids": result.source_ids,
            "tool_result": result.model_dump(),
        }
    }


def _direct_node(state: WorkflowState) -> WorkflowState:
    """Devuelve una respuesta determinista sin invocar un modelo."""
    return {
        "raw_output": {
            "route": "direct",
            "status": "ok",
            "answer": f"Recibí tu solicitud: {state['request']}",
            "source_ids": [],
            "tool_result": None,
        }
    }


def _validation_node(state: WorkflowState) -> WorkflowState:
    """Valida salida final; errores se convierten en un estado visible."""
    try:
        output = WorkflowResponse.model_validate(state["raw_output"])
        return {
            "validated_output": output.model_dump(mode="json"),
            "validation_error": None,
        }
    except Exception as error:
        return {
            "validated_output": {
                "route": state.get("route", "direct"),
                "status": "error",
                "answer": "La salida no cumplió el contrato.",
                "source_ids": [],
                "tool_result": None,
            },
            "validation_error": type(error).__name__,
        }


def build_workflow(
    *,
    checkpointer: Any | None = None,
    interrupt_before_tools: bool = False,
) -> Any:
    """Construye un workflow con rutas condicionales y validacion final.

    Pasa un checkpointer y configura un `thread_id` al invocar para conservar
    estado entre pasos. `interrupt_before_tools` permite revisar solicitudes
    antes de que el nodo de herramienta las ejecute.
    """
    graph = StateGraph(WorkflowState)
    graph.add_node("clasificador", _classify_request)
    graph.add_node("rag", _rag_node)
    graph.add_node("herramienta", _tool_node)
    graph.add_node("respuesta_directa", _direct_node)
    graph.add_node("validacion", _validation_node)

    graph.add_edge(START, "clasificador")
    graph.add_conditional_edges(
        "clasificador",
        lambda state: state["route"],
        {
            "rag": "rag",
            "tool": "herramienta",
            "direct": "respuesta_directa",
        },
    )
    graph.add_edge("rag", "validacion")
    graph.add_edge("herramienta", "validacion")
    graph.add_edge("respuesta_directa", "validacion")
    graph.add_edge("validacion", END)

    interrupt_before = ["herramienta"] if interrupt_before_tools else None
    return graph.compile(
        checkpointer=checkpointer,
        interrupt_before=interrupt_before,
    )