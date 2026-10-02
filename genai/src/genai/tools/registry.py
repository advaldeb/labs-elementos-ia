"""Herramientas locales con argumentos y resultados validados."""

from __future__ import annotations

import ast
import json
import math
import operator
import re
import unicodedata
from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, ValidationError

_COURSE_ROOT = Path(__file__).resolve().parents[3]
_SEARCH_STOP_WORDS = {"el", "la", "los", "las", "de", "del", "un", "una", "y", "en", "para"}


def _search_terms(text: str) -> set[str]:
    """Normaliza tildes y puntuacion para busquedas lexicales locales."""
    normalized = unicodedata.normalize("NFKD", text.casefold())
    without_marks = "".join(character for character in normalized if not unicodedata.combining(character))
    return set(re.findall(r"\w+", without_marks)) - _SEARCH_STOP_WORDS


class ToolName(str, Enum):
    """Nombres de herramientas que el agente puede invocar."""

    CALCULATOR = "calculadora"
    WEATHER = "clima_mock"
    PRODUCT_SEARCH = "busqueda_productos"
    DOCUMENT_SEARCH = "busqueda_documentos"


class CalculatorArgs(BaseModel):
    """Argumentos permitidos para la calculadora aritmetica."""

    model_config = ConfigDict(extra="forbid")

    expression: str = Field(min_length=1, max_length=100)


class WeatherArgs(BaseModel):
    """Argumentos para la herramienta de clima de demostracion."""

    model_config = ConfigDict(extra="forbid")

    city: str = Field(min_length=2, max_length=80)


class ProductSearchArgs(BaseModel):
    """Argumentos para buscar en el catalogo de productos simulado."""

    model_config = ConfigDict(extra="forbid")

    query: str = Field(min_length=1, max_length=100)


class DocumentSearchArgs(BaseModel):
    """Argumentos para buscar en las FAQ locales."""

    model_config = ConfigDict(extra="forbid")

    query: str = Field(min_length=2, max_length=300)


class ToolResult(BaseModel):
    """Resultado serializable de una ejecucion de herramienta."""

    tool_name: str
    success: bool
    output: str
    source_ids: list[str] = Field(default_factory=list)
    error: str | None = None


def _evaluate_expression(node: ast.AST) -> float:
    """Evalua un arbol aritmetico sin ejecutar codigo arbitrario."""
    binary_operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }
    unary_operations = {ast.UAdd: operator.pos, ast.USub: operator.neg}

    if isinstance(node, ast.Expression):
        return _evaluate_expression(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
        value = float(node.value)
        if not math.isfinite(value) or abs(value) > 1e12:
            raise ValueError("El valor excede el rango permitido.")
        return value
    if isinstance(node, ast.BinOp) and type(node.op) in binary_operations:
        left = _evaluate_expression(node.left)
        right = _evaluate_expression(node.right)
        result = binary_operations[type(node.op)](left, right)
        if not math.isfinite(result) or abs(result) > 1e12:
            raise ValueError("El resultado excede el rango permitido.")
        return result
    if isinstance(node, ast.UnaryOp) and type(node.op) in unary_operations:
        return unary_operations[type(node.op)](_evaluate_expression(node.operand))
    raise ValueError("La expresion contiene una operacion no permitida.")


def _calculate(arguments: CalculatorArgs) -> str:
    """Calcula una expresion aritmetica basica sin usar eval."""
    try:
        tree = ast.parse(arguments.expression, mode="eval")
    except SyntaxError as error:
        raise ValueError("La expresion no tiene sintaxis aritmetica valida.") from error
    if sum(1 for _ in ast.walk(tree)) > 32:
        raise ValueError("La expresion excede el limite de operaciones.")
    result = _evaluate_expression(tree)
    return f"{arguments.expression.strip()} = {result:g}"


def _weather_mock(arguments: WeatherArgs) -> str:
    """Devuelve observaciones fijas, no datos meteorologicos en tiempo real."""
    observations = {
        "santiago": "Santiago: 18 C y despejado (dato simulado).",
        "valparaiso": "Valparaiso: 16 C y nublado (dato simulado).",
    }
    return observations.get(
        arguments.city.strip().casefold(),
        f"No hay datos simulados para {arguments.city.strip()}.",
    )


def _search_products(arguments: ProductSearchArgs) -> str:
    """Busca en un catalogo local de demostracion."""
    catalog = [
        {"id": "p-101", "nombre": "Botella termica", "categoria": "accesorios"},
        {"id": "p-205", "nombre": "Mochila urbana", "categoria": "equipaje"},
        {"id": "p-310", "nombre": "Audifonos inalambricos", "categoria": "electronica"},
    ]
    terminos = set(arguments.query.casefold().split())
    resultados = [
        producto for producto in catalog
        if terminos & set(producto["nombre"].casefold().split() + [producto["categoria"]])
    ]
    return json.dumps(resultados, ensure_ascii=False)


def _search_documents(arguments: DocumentSearchArgs) -> tuple[str, list[str]]:
    """Busca FAQ locales por coincidencia de terminos y conserva sus IDs."""
    corpus_path = _COURSE_ROOT / "data" / "documents" / "faq.jsonl"
    documents = [
        json.loads(line)
        for line in corpus_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    terms = _search_terms(arguments.query)
    ranked = sorted(
        documents,
        key=lambda document: (
            -len(terms & _search_terms(document["texto"])),
            document["id"],
        ),
    )
    selected = [
        document for document in ranked
        if terms & _search_terms(document["texto"])
    ][:3]
    source_ids = [document["id"] for document in selected]
    output = "\n".join(
        f"[{document['id']}] {document['texto']}" for document in selected
    ) or "No se encontraron documentos con terminos coincidentes."
    return output, source_ids


_ARGUMENT_MODELS: dict[ToolName, type[BaseModel]] = {
    ToolName.CALCULATOR: CalculatorArgs,
    ToolName.WEATHER: WeatherArgs,
    ToolName.PRODUCT_SEARCH: ProductSearchArgs,
    ToolName.DOCUMENT_SEARCH: DocumentSearchArgs,
}


def tool_catalog() -> list[dict[str, Any]]:
    """Describe nombres y JSON Schema de herramientas disponibles."""
    descriptions = {
        ToolName.CALCULATOR: "Calcula operaciones aritmeticas basicas.",
        ToolName.WEATHER: "Consulta el clima de ejemplo; no usa datos en tiempo real.",
        ToolName.PRODUCT_SEARCH: "Busca productos en un catalogo local simulado.",
        ToolName.DOCUMENT_SEARCH: "Busca evidencia en documentos FAQ locales.",
    }
    return [
        {
            "name": name.value,
            "description": descriptions[name],
            "parameters": model.model_json_schema(),
        }
        for name, model in _ARGUMENT_MODELS.items()
    ]


def execute_tool(tool_name: str, arguments: dict[str, Any]) -> ToolResult:
    """Valida argumentos, ejecuta una herramienta permitida y devuelve resultado tipado."""
    try:
        name = ToolName(tool_name)
    except ValueError:
        return ToolResult(
            tool_name=tool_name,
            success=False,
            output="La herramienta no esta permitida.",
            error="herramienta_desconocida",
        )

    try:
        validated_arguments = _ARGUMENT_MODELS[name].model_validate(arguments)
        if name is ToolName.CALCULATOR:
            output = _calculate(validated_arguments)
            source_ids: list[str] = []
        elif name is ToolName.WEATHER:
            output = _weather_mock(validated_arguments)
            source_ids = []
        elif name is ToolName.PRODUCT_SEARCH:
            output = _search_products(validated_arguments)
            source_ids = []
        else:
            output, source_ids = _search_documents(validated_arguments)
        return ToolResult(
            tool_name=name.value,
            success=True,
            output=output,
            source_ids=source_ids,
        )
    except ValidationError:
        return ToolResult(
            tool_name=name.value,
            success=False,
            output="Los argumentos no cumplen el esquema de la herramienta.",
            error="argumentos_invalidos",
        )
    except (ValueError, ZeroDivisionError, OSError, json.JSONDecodeError) as error:
        return ToolResult(
            tool_name=name.value,
            success=False,
            output="La herramienta no pudo completar la operacion.",
            error=type(error).__name__,
        )