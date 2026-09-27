"""Pruebas del workflow LangGraph y sus rutas condicionales."""

from langgraph.checkpoint.memory import MemorySaver

from llm_engineering.agents.graph import build_workflow


def test_workflow_routes_rag_tool_and_direct_requests() -> None:
    workflow = build_workflow()
    casos = [
        ({"request": "devolucion 30 dias"}, "rag"),
        ({"request": "calcula 2 + 3"}, "tool"),
        ({"request": "hola, necesito ayuda"}, "direct"),
    ]

    for entrada, ruta_esperada in casos:
        resultado = workflow.invoke(entrada)

        assert resultado["validated_output"]["route"] == ruta_esperada
        assert resultado["validated_output"]["status"] == "ok"
        assert resultado["validation_error"] is None


def test_rag_route_returns_source_ids() -> None:
    workflow = build_workflow()

    resultado = workflow.invoke({"request": "devolucion 30 dias"})

    assert "devolucion_plazo" in resultado["validated_output"]["source_ids"]


def test_workflow_interrupts_before_tool_and_resumes_with_checkpoint() -> None:
    workflow = build_workflow(
        checkpointer=MemorySaver(),
        interrupt_before_tools=True,
    )
    config = {"configurable": {"thread_id": "revision-humana"}}

    pausado = workflow.invoke({"request": "calcula 2 + 3"}, config)
    assert pausado["route"] == "tool"
    assert "raw_output" not in pausado

    reanudado = workflow.invoke(None, config)
    assert reanudado["validated_output"]["route"] == "tool"
    assert reanudado["validated_output"]["tool_result"]["output"] == "2 + 3 = 5"