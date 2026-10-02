"""Herramientas con contratos de entrada validados."""

from genai.tools.registry import (
	CalculatorArgs,
	DocumentSearchArgs,
	ProductSearchArgs,
	ToolName,
	ToolResult,
	WeatherArgs,
	execute_tool,
	tool_catalog,
)

__all__ = [
	"CalculatorArgs",
	"DocumentSearchArgs",
	"ProductSearchArgs",
	"ToolName",
	"ToolResult",
	"WeatherArgs",
	"execute_tool",
	"tool_catalog",
]