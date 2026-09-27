"""Pruebas sin red de observabilidad opcional y Agentic RAG acotado."""

import pytest
from types import SimpleNamespace

from llm_engineering.agents import build_agentic_rag, run_agentic_rag
from llm_engineering.observability import (
    langsmith_tracing,
    load_langsmith_settings,
    traceable_if_enabled,
)


def test_langsmith_is_disabled_without_explicit_setting() -> None:
    settings = load_langsmith_settings({})

    assert settings.enabled is False
    assert settings.api_key_configured is False
    with langsmith_tracing():
        assert True


def test_langsmith_rejects_enabled_tracing_without_key() -> None:
    with pytest.raises(ValueError, match="LANGSMITH_API_KEY"):
        with langsmith_tracing(enabled=True):
            pass


def test_traceable_decorator_is_passthrough_when_disabled(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LANGSMITH_TRACING", "false")

    @traceable_if_enabled(name="funcion_local")
    def suma(left: int, right: int) -> int:
        return left + right

    assert suma(2, 3) == 5


def test_agentic_rag_answers_supported_query_with_sources() -> None:
    result = run_agentic_rag("seguimiento paquete")
    output = result["validated_output"]

    assert output["status"] == "answered"
    assert "envio_seguimiento" in output["source_ids"]
    assert output["retrieval_attempts"] == 1
    assert output["generation_mode"] == "extractive"
    assert output["llm_calls"] == 0


def test_agentic_rag_graph_has_router_decision_and_generation_nodes() -> None:
    node_names = set(build_agentic_rag().get_graph().nodes)

    assert {"router", "reescribir", "recuperar", "evaluar_documentos"} <= node_names
    assert {"decision_contexto", "responder", "validar_respuesta", "abstenerse"} <= node_names


def test_agentic_rag_routes_out_of_domain_request_directly() -> None:
    result = run_agentic_rag("hola, necesito ayuda")
    output = result["validated_output"]

    assert output["route"] == "direct"
    assert output["retrieval_attempts"] == 0
    assert output["llm_calls"] == 0


def test_agentic_rag_optional_generation_uses_one_model_call(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    class ModeloSimulado:
        def invoke(self, messages: object) -> SimpleNamespace:
            return SimpleNamespace(content="Revisa el código de rastreo en el correo.")

    monkeypatch.setattr(
        "llm_engineering.models.get_llm",
        lambda provider, model=None, temperature=None: ModeloSimulado(),
    )

    result = run_agentic_rag(
        "seguimiento paquete",
        generate_with_llm=True,
    )
    output = result["validated_output"]

    assert output["generation_mode"] == "llm"
    assert output["llm_calls"] == 1
    assert output["status"] == "answered"


def test_agentic_rag_rewrites_query_after_no_evidence() -> None:
    result = run_agentic_rag("quiero que me regresen el dinero")
    output = result["validated_output"]

    assert output["status"] == "answered"
    assert output["retrieval_attempts"] == 2
    assert len(result["query_history"]) == 2
    assert "reembolso" in result["query_history"][1]


def test_agentic_rag_abstains_at_retrieval_limit() -> None:
    result = run_agentic_rag("xyzzy qqqv", max_retrievals=1, force_rag=True)
    output = result["validated_output"]

    assert output["status"] == "abstained"
    assert output["retrieval_attempts"] == 1


def test_agentic_rag_rejects_zero_retrieval_budget() -> None:
    with pytest.raises(ValueError, match="max_retrievals"):
        run_agentic_rag("pregunta", max_retrievals=0)