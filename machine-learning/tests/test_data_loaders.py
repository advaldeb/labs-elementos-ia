import pytest

from ml_course.data import get_data_path
from ml_course.data.loaders import get_project_root


def test_project_root_is_independent_of_working_directory(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)

    assert (get_project_root() / "pyproject.toml").is_file()


def test_data_path_resolves_inside_requested_category():
    path = get_data_path("example.csv", category="external")

    assert path == get_project_root() / "data" / "external" / "example.csv"


def test_data_path_rejects_unknown_category():
    with pytest.raises(ValueError, match="Categoría"):
        get_data_path("example.csv", category="unknown")


def test_data_path_rejects_path_traversal():
    with pytest.raises(ValueError, match="permanecer"):
        get_data_path("..", "secret.csv", category="external")