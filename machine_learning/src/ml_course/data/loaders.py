from pathlib import Path

_DATA_CATEGORIES = {"raw", "processed", "external"}


def get_project_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "pyproject.toml").is_file():
            return parent
    raise RuntimeError("No se pudo localizar la raíz del repositorio del curso.")


def get_data_path(*parts: str, category: str = "raw") -> Path:
    if category not in _DATA_CATEGORIES:
        raise ValueError(f"Categoría de datos no válida: {category}")

    data_directory = (get_project_root() / "data" / category).resolve()
    path = data_directory.joinpath(*parts).resolve()
    try:
        path.relative_to(data_directory)
    except ValueError as error:
        raise ValueError("La ruta del dataset debe permanecer dentro de su categoría.") from error
    return path