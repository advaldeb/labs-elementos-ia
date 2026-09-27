"""Inicializacion compartida del entorno de notebooks."""

from pathlib import Path

from dotenv import load_dotenv

_COURSE_ROOT = Path(__file__).resolve().parents[2]


def preparar_entorno() -> Path:
    """Carga `.env` sin reemplazar variables existentes y devuelve la raiz del curso."""
    load_dotenv(_COURSE_ROOT / ".env", override=False)
    return _COURSE_ROOT