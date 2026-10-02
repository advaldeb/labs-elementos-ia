"""Adaptadores LangChain para las herramientas locales del curso."""

from langchain_core.tools import StructuredTool

from genai.tools.registry import (
    CalculatorArgs,
    DocumentSearchArgs,
    ProductSearchArgs,
    ToolName,
    WeatherArgs,
    execute_tool,
)


def crear_herramientas_langchain() -> list[StructuredTool]:
    """Adapta herramientas validadas a la interfaz de LangChain."""
    def calcular(expression: str) -> str:
        return execute_tool(ToolName.CALCULATOR.value, {"expression": expression}).output

    def consultar_clima(city: str) -> str:
        return execute_tool(ToolName.WEATHER.value, {"city": city}).output

    def buscar_productos(query: str) -> str:
        return execute_tool(ToolName.PRODUCT_SEARCH.value, {"query": query}).output

    def buscar_documentos(query: str) -> str:
        return execute_tool(ToolName.DOCUMENT_SEARCH.value, {"query": query}).output

    return [
        StructuredTool.from_function(
            func=calcular,
            name=ToolName.CALCULATOR.value,
            description="Calcula operaciones aritmeticas basicas.",
            args_schema=CalculatorArgs,
        ),
        StructuredTool.from_function(
            func=consultar_clima,
            name=ToolName.WEATHER.value,
            description="Consulta el clima de ejemplo, no datos en tiempo real.",
            args_schema=WeatherArgs,
        ),
        StructuredTool.from_function(
            func=buscar_productos,
            name=ToolName.PRODUCT_SEARCH.value,
            description="Busca productos en el catalogo local simulado.",
            args_schema=ProductSearchArgs,
        ),
        StructuredTool.from_function(
            func=buscar_documentos,
            name=ToolName.DOCUMENT_SEARCH.value,
            description="Busca evidencia en las FAQ locales.",
            args_schema=DocumentSearchArgs,
        ),
    ]