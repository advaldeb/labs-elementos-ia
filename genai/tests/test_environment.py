"""Pruebas del arranque compartido de los notebooks."""

from pathlib import Path

from llm_engineering.environment import preparar_entorno


def test_preparar_entorno_devuelve_la_raiz_del_curso() -> None:
    """La raiz incluye el manifiesto y las carpetas usadas por los laboratorios."""
    raiz_curso = preparar_entorno()

    assert (raiz_curso / "pyproject.toml").is_file()
    assert (raiz_curso / "notebooks").is_dir()
    assert raiz_curso == Path(__file__).resolve().parents[1]