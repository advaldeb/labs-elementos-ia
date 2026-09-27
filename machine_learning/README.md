# Machine Learning

Repositorio de apoyo para un curso universitario de Machine Learning. Reúne notebooks de Jupyter para estudiar aprendizaje no supervisado, reducción de dimensionalidad, regresión, modelos basados en árboles, series de tiempo y segmentación de clientes. El curso complementario de LLM Engineering se conserva en `10 llm-eng/`.

## Objetivos del curso

- Comprender y comparar familias de métodos de aprendizaje automático.
- Diseñar flujos de análisis reproducibles desde los datos hasta la evaluación.
- Interpretar resultados y reconocer supuestos, limitaciones y riesgos de cada método.
- Practicar experimentación computacional con Python y Jupyter.

## Resultados de aprendizaje

Al finalizar, el estudiantado podrá seleccionar métodos acordes al problema, preparar datos sin introducir Data Leakage, ajustar y evaluar modelos con métricas apropiadas, interpretar resultados y comunicar conclusiones basadas en evidencia.

## Contenidos

1. [Clustering](notebooks/01_clustering/)
2. [Reducción de dimensionalidad](notebooks/02_dimensionality_reduction/)
3. [Modelos lineales](notebooks/03_linear_models/)
4. [Modelos basados en árboles](notebooks/04_tree_based_models/)
5. [Clasificación](notebooks/05_classification/) (módulo preparado para material futuro)
6. [Series de tiempo](notebooks/06_time_series/)
7. [Selección y evaluación de modelos](notebooks/07_model_selection/) (módulo preparado para material futuro)
8. [Segmentación de clientes](notebooks/08_customer_segmentation/)

## Estructura del repositorio

- `notebooks/`: material de clase, agrupado por tema y numerado localmente.
- `data/`: datos originales, procesados y externos; los datos no se ignoran en Git.
- `src/`: utilidades Python reutilizables del curso, instalables como paquete.
- `exercises/` y `solutions/`: espacios paralelos para actividades y soluciones docentes.
- `tests/`: pruebas del código reutilizable de `src/`.
- `docs/`: guía académica, ruta de aprendizaje, entorno, datasets y bibliografía.
- `assets/`: imágenes, diagramas y figuras para el material docente.
- `10 llm-eng/`: curso de LLM Engineering preservado como subproyecto independiente.

## Instalación

Se recomienda Python 3.11 o 3.12. Desde la raíz del repositorio, crea un entorno virtual y luego instala las dependencias:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

En macOS o Linux, activa el entorno con `source .venv/bin/activate`. El manifiesto incluye dependencias de los módulos ML y del subproyecto LLM; algunos proveedores de modelos requieren configuración adicional y servicios externos.

## Configuración del entorno

Duplica `.env.example` como `.env` solo si usarás proveedores de LLM que requieren credenciales. Mantén las claves fuera de Git. Para detalles del entorno, consulta [docs/environment_setup.md](docs/environment_setup.md).

## Ejecución de notebooks

Abre la raíz del repositorio en JupyterLab o Visual Studio Code, selecciona el kernel del entorno `.venv` y ejecuta las celdas en orden. Para que `ml_course` esté disponible, instala el proyecto con `python -m pip install -e .` (ya incluido en `requirements.txt`). Los loaders usan `pathlib` y resuelven los datos desde la raíz del proyecto, no desde el directorio de trabajo.

## Datasets

El catálogo está en [data/README.md](data/README.md) y [docs/datasets.md](docs/datasets.md). Los archivos de `data/raw/` son entradas originales, `data/external/` conserva recursos de terceros y `data/processed/` se reserva para derivados. Algunos recursos originales están incompletos; las limitaciones conocidas están documentadas en el catálogo y en [REORGANIZATION_REPORT.md](REORGANIZATION_REPORT.md).

## Convenciones

- Rutas técnicas y nombres de archivos en inglés; explicaciones pedagógicas en español.
- Numeración local dentro de cada módulo.
- No modificar directamente los datasets originales.
- Mantener visibles en los notebooks los pasos relevantes para el aprendizaje; abstraer solo lógica claramente reutilizable.
- Revisar [docs/datasets.md](docs/datasets.md) antes de asumir que un recurso de terceros está disponible.

## Ruta de aprendizaje

La progresión conceptual se describe en [docs/learning_path.md](docs/learning_path.md); la descripción académica completa está en [docs/course_overview.md](docs/course_overview.md).

## Bibliografía

La bibliografía recomendada y los recursos oficiales están centralizados en [docs/references.md](docs/references.md).

## Licencia

Consulta [LICENSE](LICENSE).
