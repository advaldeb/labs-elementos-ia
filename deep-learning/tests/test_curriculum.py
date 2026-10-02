import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"
MODULES = {
    "lab_00_foundations": ["00_introduction_to_deep_learning", "01_tensors_and_autograd"],
    "lab_01_neural_networks": ["02_neuron_and_perceptron", "03_multilayer_perceptron_numpy", "04_forward_propagation", "05_backpropagation"],
    "lab_02_training": ["06_loss_functions", "07_gradient_descent", "08_optimizers_and_training_loop"],
    "lab_03_generalization": ["09_activation_functions", "10_weight_initialization", "11_regularization_and_generalization"],
    "lab_04_computer_vision": ["12_convolutions", "13_convolutional_neural_networks", "14_transfer_learning"],
    "lab_05_sequences": ["15_recurrent_neural_networks", "16_lstm_and_gru", "17_attention_mechanism"],
    "lab_06_transformers": ["18_transformer_fundamentals"],
    "lab_07_capstone": ["19_deep_learning_capstone"],
    "lab_08_business_models": ["20_tabular_embeddings_churn", "21_neural_recommender", "22_time_series_forecasting"],
    "lab_09_business_applications": ["23_image_quality_inspection", "24_autoencoder_anomaly_detection",
                                     "25_text_ticket_classification", "26_siamese_entity_resolution"],
}


def test_notebook_inventory_matches_course_sequence():
    expected = {f"{module}/{name}.ipynb" for module, names in MODULES.items() for name in names}
    actual = {path.relative_to(NOTEBOOKS).as_posix() for path in NOTEBOOKS.rglob("*.ipynb")}
    assert actual == expected


def test_notebooks_have_language_metadata_and_three_exercises():
    for path in NOTEBOOKS.rglob("*.ipynb"):
        notebook = json.loads(path.read_text(encoding="utf-8"))
        markdown = []
        for cell in notebook["cells"]:
            assert cell.get("metadata", {}).get("language") in {"python", "markdown"}
            source = "".join(cell.get("source", []))
            if cell["cell_type"] == "code":
                ast.parse(source, filename=f"{path.name}:{cell.get('metadata', {}).get('id', '?')}")
            elif cell["cell_type"] == "markdown":
                markdown.append(source)
        text = "\n".join(markdown)
        assert "**Guiado:**" in text, path
        assert "**Independiente:**" in text, path
        assert "**Desafío:**" in text, path


def test_each_notebook_has_a_separate_instructor_solution():
    for module, names in MODULES.items():
        solution_path = ROOT / "solutions" / f"{module}.md"
        solution = solution_path.read_text(encoding="utf-8")
        for name in names:
            assert f"`{name}.ipynb`" in solution, name