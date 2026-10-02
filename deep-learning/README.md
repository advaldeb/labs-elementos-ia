# Laboratorios de Deep Learning

Curso práctico de redes neuronales: parte de tensores y perceptrones, construye los mecanismos fundamentales con NumPy y pasa gradualmente a PyTorch para entrenamiento, visión, secuencias y Transformers. Las explicaciones, comentarios, ejercicios e interpretaciones están en español; los nombres técnicos permanecen en inglés.

## Estructura

- `notebooks/`: veintisiete laboratorios ejecutables y ordenados por tema.
- `data/`: catálogo y política de datos; los ejemplos principales son sintéticos.
- `docs/`: decisiones docentes, reproducibilidad y guía de ejecución.
- `exercises/`: orientación a las actividades incluidas en cada notebook.
- `solutions/`: claves docentes separadas e identificadas por laboratorio.
- `tests/`: validaciones de estructura, metadatos, ejercicios y sintaxis Python.
- `assets/`: las figuras se generan en los notebooks; no se requieren imágenes externas.
- `src/`: no se incluye paquete auxiliar: mantener explícitos los pasos es parte del objetivo.

## Requisitos e instalación

Se recomienda Python 3.11 o 3.12. Desde la raíz del repositorio:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r deep-learning/requirements.txt
```

En macOS o Linux, activa el entorno con `source .venv/bin/activate`. PyTorch seleccionará CPU automáticamente; una GPU compatible es opcional. Para instalar el proyecto como paquete de desarrollo, usa `python -m pip install -e deep-learning[dev]`.

## Orden de ejecución

Abre la raíz del repositorio en VS Code/Jupyter, selecciona el kernel `.venv` y ejecuta las celdas en orden. Cada notebook genera datos pequeños localmente y fija semillas. Ajusta normalizaciones con entrenamiento; usa validación para decisiones y reserva test para la evaluación final. El laboratorio 14 estudia transferencia entre tareas con una CNN sintética local, sin pesos externos. El laboratorio 19 integra una comparación MLP/CNN con imágenes generadas, también sin recursos externos. Los laboratorios 20 a 22 aplican los modelos a problemas de negocio con datos sintéticos: fuga de clientes con embeddings, recomendación y pronóstico de demanda. Los laboratorios 23 a 26 cubren inspección visual de calidad, detección de anomalías, clasificación de tickets y detección de clientes duplicados.

## Ruta de laboratorios

| Lab | Notebook | Propósito |
|---|---|---|
| 00 | `lab_00_foundations/00_introduction_to_deep_learning.ipynb` | Ciclo de aprendizaje, baseline y generalización. |
| 01 | `lab_00_foundations/01_tensors_and_autograd.ipynb` | Tensores, formas, dispositivos y derivación automática. |
| 02 | `lab_01_neural_networks/02_neuron_and_perceptron.ipynb` | Neurona, frontera lineal, AND y límite de XOR. |
| 03 | `lab_01_neural_networks/03_multilayer_perceptron_numpy.ipynb` | Forward y retropropagación NumPy en XOR. |
| 04 | `lab_01_neural_networks/04_forward_propagation.ipynb` | Formas e implementación equivalente con PyTorch. |
| 05 | `lab_01_neural_networks/05_backpropagation.ipynb` | Regla de la cadena y gradientes. |
| 06 | `lab_02_training/06_loss_functions.ipynb` | Pérdidas de regresión y clasificación. |
| 07 | `lab_02_training/07_gradient_descent.ipynb` | Gradiente, tasa de aprendizaje y trayectoria. |
| 08 | `lab_02_training/08_optimizers_and_training_loop.ipynb` | SGD, momentum y Adam bajo condiciones comunes. |
| 09 | `lab_03_generalization/09_activation_functions.ipynb` | Activaciones, saturación y gradientes. |
| 10 | `lab_03_generalization/10_weight_initialization.ipynb` | Inicialización y propagación de activaciones. |
| 11 | `lab_03_generalization/11_regularization_and_generalization.ipynb` | Sobreajuste, weight decay y dropout. |
| 12 | `lab_04_computer_vision/12_convolutions.ipynb` | Correlación 2D, kernels y mapas de características. |
| 13 | `lab_04_computer_vision/13_convolutional_neural_networks.ipynb` | CNN, evaluación y errores de clasificación. |
| 14 | `lab_04_computer_vision/14_transfer_learning.ipynb` | Congelar y adaptar representaciones entre tareas. |
| 15 | `lab_05_sequences/15_recurrent_neural_networks.ipynb` | Recurrencia, estado oculto y secuencias. |
| 16 | `lab_05_sequences/16_lstm_and_gru.ipynb` | Compuertas y memoria recurrente. |
| 17 | `lab_05_sequences/17_attention_mechanism.ipynb` | Consultas, claves, valores y pesos de atención. |
| 18 | `lab_06_transformers/18_transformer_fundamentals.ipynb` | Posición, atención multi-cabeza y encoder Transformer. |
| 19 | `lab_07_capstone/19_deep_learning_capstone.ipynb` | Proyecto integrador y comparación MLP/CNN. |
| 20 | `lab_08_business_models/20_tabular_embeddings_churn.ipynb` | Embeddings para datos tabulares y priorización de fuga de clientes. |
| 21 | `lab_08_business_models/21_neural_recommender.ipynb` | Factorización matricial y NCF con muestreo negativo para recomendación. |
| 22 | `lab_08_business_models/22_time_series_forecasting.ipynb` | Pronóstico de demanda con MLP, CNN 1D y LSTM frente a baselines. |
| 23 | `lab_09_business_applications/23_image_quality_inspection.ipynb` | CNN, aumento de datos, umbral por costo y saliencia para inspección de calidad. |
| 24 | `lab_09_business_applications/24_autoencoder_anomaly_detection.ipynb` | Autoencoder frente a z-score y Mahalanobis para transacciones anómalas. |
| 25 | `lab_09_business_applications/25_text_ticket_classification.ipynb` | Enmascarado de PII, bolsa de embeddings y Transformer para enrutar tickets. |
| 26 | `lab_09_business_applications/26_siamese_entity_resolution.ipynb` | Red siamesa con trigramas para detectar clientes duplicados. |

## Pruebas

Desde la raíz, ejecuta `python -m pytest deep-learning/tests`. Las pruebas validan inventario, idioma de las celdas, tres ejercicios y sintaxis Python. Para validar resultados numéricos, ejecuta los notebooks en orden con el kernel instalado.

## Datos externos y pesos

No se almacenan credenciales, datasets grandes ni pesos descargados. Los laboratorios generan sus datos en memoria. Si se amplía transferencia con pesos preentrenados, esa variante debe ser opcional, declarar fuente/licencia y conservar una alternativa local.