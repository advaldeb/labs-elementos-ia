"""Pruebas de herramientas y bucle manual de agente sin llamadas externas."""

import json

from llm_engineering.agents import run_agent
from llm_engineering.tools import ToolName, execute_tool, tool_catalog


def _decisiones(*payloads: dict[str, object]):
    """Crea un decisor determinista para recorrer una secuencia de casos."""
    pendientes = iter(json.dumps(payload) for payload in payloads)
    return lambda request, observations: next(pendientes)


def test_calculator_executes_only_safe_arithmetic() -> None:
    resultado = execute_tool(ToolName.CALCULATOR.value, {"expression": "12 * (3 + 2)"})

    assert resultado.success
    assert resultado.output == "12 * (3 + 2) = 60"
    assert not execute_tool(ToolName.CALCULATOR.value, {"expression": "__import__('os')"}).success
    assert not execute_tool(ToolName.CALCULATOR.value, {"expression": "1e999"}).success


def test_tools_validate_arguments_and_return_mock_data() -> None:
    clima = execute_tool(ToolName.WEATHER.value, {"city": "Santiago"})
    invalid = execute_tool(ToolName.WEATHER.value, {"ciudad": "Santiago"})
    productos = execute_tool(ToolName.PRODUCT_SEARCH.value, {"query": "mochila"})
    documentos = execute_tool(ToolName.DOCUMENT_SEARCH.value, {"query": "devolucion 30 dias"})

    assert clima.success and "simulado" in clima.output
    assert not invalid.success and invalid.error == "argumentos_invalidos"
    assert productos.success and "Mochila urbana" in productos.output
    assert documentos.success and "devolucion_plazo" in documentos.source_ids
    assert len(tool_catalog()) == 4


def test_manual_agent_executes_tool_then_finishes() -> None:
    run = run_agent(
        "Calcula dos mas tres",
        _decisiones(
            {"action": "tool", "tool_name": "calculadora", "arguments": {"expression": "2 + 3"}},
            {"action": "final", "final_answer": "El resultado es 5."},
        ),
    )

    assert run.status == "completed"
    assert run.answer == "El resultado es 5."
    assert run.steps[0]["output"] == "2 + 3 = 5"


def test_manual_agent_stops_hallucinated_tool_and_repeated_call() -> None:
    hallucinated = run_agent(
        "Consulta",
        _decisiones({"action": "tool", "tool_name": "herramienta_fantasma", "arguments": {}}),
    )
    repeated = run_agent(
        "Consulta",
        _decisiones(
            {"action": "tool", "tool_name": "calculadora", "arguments": {"expression": "1 + 1"}},
            {"action": "tool", "tool_name": "calculadora", "arguments": {"expression": "1 + 1"}},
        ),
    )

    assert hallucinated.status == "unknown_tool"
    assert repeated.status == "repeated_call"


def test_manual_agent_reports_invalid_decision_and_step_limit() -> None:
    invalid = run_agent("Consulta", lambda request, observations: "esto no es JSON")
    limited = run_agent(
        "Consulta",
        _decisiones({"action": "tool", "tool_name": "calculadora", "arguments": {"expression": "1 + 1"}}),
        max_steps=1,
    )

    assert invalid.status == "invalid_decision"
    assert limited.status == "max_steps"