# Informe de reorganización

## 1. Resumen ejecutivo

Se reorganizó el material de Machine Learning en módulos técnicos en inglés y numeración local. Se migraron 21 notebooks existentes, se centralizaron cuatro datasets utilizables y se conservaron los dos ZIP legacy sin alterarlos. Se añadió un paquete pequeño `ml_course` para resolver rutas desde cualquier directorio de trabajo, junto con tests, dependencias, estructura docente y documentación en español.

El subproyecto `10 llm-eng/` (27 notebooks, código, pruebas, configuración, corpus y resultados) permanece en su ubicación y conserva su estructura independiente. No se crearon notebooks, datasets ni ejercicios ficticios. Los notebooks no fueron ejecutados de extremo a extremo.

## 2. Estructura anterior

- `01 clustering/`: tres notebooks y un manifiesto de dependencias extenso.
- `02 pca and fa/`: dos notebooks.
- `03 regression/`: cuatro notebooks, un notebook importado de Kaggle, un CSV eléctrico, un calendario M5 y dos ZIP.
- `04 treemodels/`: cuatro notebooks.
- `06 time series/`: seis notebooks.
- `08 customer-segmentaion/`: un notebook y dos archivos llamados `.json` que en realidad están en formato JSON Lines.
- `09 deep-learning/`: carpeta vacía.
- `10 llm-eng/`: subproyecto independiente con 27 notebooks, 28 módulos/archivos Python, seis tests, configuración, datos y CSV de resultados.
- Raíz: README general y LICENSE; no existía `.gitignore` raíz ni catálogo central de datos.

El inventario inicial contenía 48 notebooks, 57 CSV, 28 archivos `.py`, dos JSON, un JSONL y dos ZIP, además de metadata y archivos auxiliares. No se encontraron Excel ni Parquet.

## 3. Estructura nueva

```text
README.md
LICENSE
.gitignore
.env.example
pyproject.toml
requirements.txt
REORGANIZATION_REPORT.md
docs/
  course_overview.md
  learning_path.md
  environment_setup.md
  datasets.md
  references.md
  legacy/
data/
  README.md
  raw/
  processed/
  external/
    electricity_consumption_and_production.csv
    m5_calendar.csv
    starbucks_portfolio.jsonl
    starbucks_profile.jsonl
    legacy/
      archive.zip
      m5-forecasting-accuracy.zip
notebooks/
  01_clustering/                 (3 notebooks)
  02_dimensionality_reduction/   (2 notebooks)
  03_linear_models/              (4 notebooks)
  04_tree_based_models/          (4 notebooks)
  05_classification/             (sin notebooks)
  06_time_series/                (7 notebooks)
  07_model_selection/            (sin notebooks)
  08_customer_segmentation/      (1 notebook)
  09_deep_learning/              (sin notebooks)
src/ml_course/
  data/loaders.py
  features/
  models/
  visualization/
  utils/
exercises/                        (9 módulos vacíos preparados)
solutions/                        (9 módulos vacíos preparados)
tests/test_data_loaders.py
assets/{images,diagrams,figures}/
10 llm-eng/                       (subproyecto preservado)
```

Los módulos futuros se mantienen vacíos y están marcados con `.gitkeep`; no contienen notebooks inventados.

## 4. Archivos movidos y renombrados

| Ruta anterior | Ruta nueva |
|---|---|
| `01 clustering/01 kmeans.ipynb` | `notebooks/01_clustering/01_kmeans.ipynb` |
| `01 clustering/02 hierarchical.ipynb` | `notebooks/01_clustering/02_hierarchical_clustering.ipynb` |
| `01 clustering/03 gmmclust.ipynb` | `notebooks/01_clustering/03_gaussian_mixture_models.ipynb` |
| `02 pca and fa/04 pca.ipynb` | `notebooks/02_dimensionality_reduction/01_pca.ipynb` |
| `02 pca and fa/05 fa.ipynb` | `notebooks/02_dimensionality_reduction/02_factor_analysis.ipynb` |
| `03 regression/06 regression.ipynb` | `notebooks/03_linear_models/01_linear_regression.ipynb` |
| `03 regression/07 regression ridge.ipynb` | `notebooks/03_linear_models/02_ridge_regression.ipynb` |
| `03 regression/08 regression lasso.ipynb` | `notebooks/03_linear_models/03_lasso_regression.ipynb` |
| `03 regression/09 regression elasticnet.ipynb` | `notebooks/03_linear_models/04_elastic_net.ipynb` |
| `04 treemodels/10 regressiontree.ipynb` | `notebooks/04_tree_based_models/01_regression_trees.ipynb` |
| `04 treemodels/11 randomforest.ipynb` | `notebooks/04_tree_based_models/02_random_forest.ipynb` |
| `04 treemodels/12 gbm.ipynb` | `notebooks/04_tree_based_models/03_gradient_boosting.ipynb` |
| `04 treemodels/13 xgboost.ipynb` | `notebooks/04_tree_based_models/04_xgboost.ipynb` |
| `06 time series/12 regespuriats.ipynb` | `notebooks/06_time_series/01_spurious_regressions.ipynb` |
| `06 time series/13 distributed lag model.ipynb` | `notebooks/06_time_series/02_distributed_lag_models.ipynb` |
| `06 time series/14 holt-winters.ipynb` | `notebooks/06_time_series/03_holt_winters.ipynb` |
| `06 time series/15 ETS.ipynb` | `notebooks/06_time_series/04_ets.ipynb` |
| `03 regression/code/timeseries-forecasting-with-regression-and-prophet.ipynb` | `notebooks/06_time_series/05_prophet_forecasting.ipynb` |
| `06 time series/17 SARIMA.ipynb` | `notebooks/06_time_series/06_sarima.ipynb` |
| `06 time series/16 Prophet.ipynb` | `notebooks/06_time_series/07_structural_time_series_legacy.ipynb` |
| `08 customer-segmentaion/customer_segmentation.ipynb` | `notebooks/08_customer_segmentation/01_customer_segmentation.ipynb` |
| `03 regression/code/electricityConsumptionAndProductioction.csv` | `data/external/electricity_consumption_and_production.csv` |
| `03 regression/data/calendar.csv` | `data/external/m5_calendar.csv` |
| `08 customer-segmentaion/data/portfolio.json` | `data/external/starbucks_portfolio.jsonl` |
| `08 customer-segmentaion/data/profile.json` | `data/external/starbucks_profile.jsonl` |
| `03 regression/code/archive.zip` | `data/external/legacy/archive.zip` |
| `03 regression/data/m5-forecasting-accuracy.zip` | `data/external/legacy/m5-forecasting-accuracy.zip` |
| `01 clustering/requirements.txt` | `docs/legacy/clustering-requirements-original.txt` |

`LICENSE` se conserva sin cambios. `10 llm-eng/` no se movió para evitar alterar sus rutas de configuración, importación y resultados.

## 5. Datasets reorganizados

El catálogo completo está en [data/README.md](data/README.md). Los cuatro datasets utilizables son el CSV eléctrico, el calendario M5 y los JSONL de portafolio y perfiles Starbucks. El calendario M5 no tenía referencias en los notebooks actuales.

Los dos ZIP son archivos ZIP válidos de 22 bytes sin miembros. Se preservaron byte por byte en `data/external/legacy/`; no se descomprimieron ni reemplazaron. El notebook de segmentación también requiere `starbucks_transcript.jsonl`, que no estaba en el repositorio.

El corpus `10 llm-eng/data/documents/faq.jsonl` y los CSV de resultados del subproyecto LLM permanecen en sus ubicaciones originales; los resultados no son datasets fuente del curso ML.

## 6. Dependencias consolidadas

`requirements.txt` instala el paquete raíz en modo editable con sus dependencias de ejecución y desarrollo (`-e .[dev]`). `pyproject.toml` declara dependencias directas de los notebooks ML y del subproyecto LLM, entre ellas NumPy, pandas, SciPy, Matplotlib, seaborn, statsmodels, scikit-learn, XGBoost, Prophet, pmdarima, OpenML, ucimlrepo, Jupyter, Pydantic, LangChain, LangGraph y LangSmith; pytest queda en el extra `dev`.

`10 llm-eng/requirements.txt` y `10 llm-eng/pyproject.toml` se mantienen para permitir instalar ese subproyecto por separado. El manifiesto legado de clustering se archivó porque incluía numerosos paquetes no vinculados con ese módulo. Las versiones se expresan como rangos compatibles; no se añadió un lockfile.

## 7. Cambios en rutas

Se añadió `src/ml_course/data/loaders.py`. `get_project_root()` descubre la raíz desde la ubicación del paquete, y `get_data_path()` resuelve archivos bajo `data/raw`, `data/processed` o `data/external`, validando que no se escape de su categoría.

Se actualizaron los loaders de los 13 notebooks de regresión, árboles y series de tiempo que cargan el CSV eléctrico, además del notebook histórico de Prophet y el de segmentación. Las lecturas usan `pathlib` y ya no dependen de rutas relativas al directorio actual ni de `/kaggle/input`.

## 8. Problemas encontrados

- Falta `starbucks_transcript.jsonl`; el notebook de segmentación no puede completar la lectura de datos hasta recuperar ese recurso desde una fuente autorizada.
- Los dos ZIP conservados están vacíos y no aportan los datasets anunciados por sus nombres.
- El archivo anteriormente llamado `16 Prophet.ipynb` importa `UnobservedComponents` de statsmodels, no Prophet. Se conservó como laboratorio estructural legacy. El notebook de origen Kaggle sí importa Prophet y ocupa la posición local 05.
- El calendario M5 existe pero ningún notebook actual lo utiliza; no se añadieron las tablas de datos que suelen acompañar la competencia.
- En el Python activo de esta sesión faltan `xgboost`, `prophet`, `pmdarima`, `openml`, `ucimlrepo` y `jupyterlab`. Se declaran en el manifiesto raíz, pero no se instalaron ni se comprobó su instalación completa.
- Parte de los notebooks consulta servicios o datos remotos, por lo que su ejecución completa depende de red y, en algunos casos, de credenciales. No se ejecutaron notebooks completos.
- Algunas carpetas fuente vacías permanecen en el directorio local por bloqueos de Windows; no contienen archivos y no forman parte del árbol versionado.

## 9. Deuda técnica

- Varios notebooks repiten preparación, evaluación y visualización; se dejaron visibles por su valor pedagógico. Revisar una extracción gradual de helpers solo tras estabilizar los pasos docentes.
- Hay que confirmar procedencia, licencia y versión de cada dataset externo y recuperar los recursos faltantes.
- El notebook histórico de Kaggle conserva secciones y comentarios en inglés; no se normalizó el contenido pedagógico en esta iteración.
- Los rangos de versiones permiten resolver dependencias nuevas y no garantizan un entorno idéntico en el tiempo; falta decidir una política de lockfile y matriz de Python.
- No hay todavía validación automatizada de ejecución de notebooks ni CI.

## 10. Validación realizada

- `python -m pytest -q`: 4 pruebas aprobadas para descubrimiento de raíz, rutas de datos, categorías y traversal.
- Se parseó el TOML y se validaron como JSON los 21 notebooks ML.
- Se transformaron celdas con la sintaxis IPython y se analizaron 267 celdas de código; se inspeccionaron rutas obsoletas y se comprobó que el CSV eléctrico existe en su nueva ruta.
- Se comprobaron los enlaces locales Markdown después de crear este informe; no hay enlaces rotos.
- Los datasets no están ignorados por el `.gitignore` raíz.
- `get_errors` no encontró errores en `src/` ni `tests/`.

Estas comprobaciones son estáticas y focalizadas; no equivalen a ejecutar todos los notebooks en un entorno limpio.

## 11. Recomendaciones para la siguiente iteración

1. Recuperar el transcript Starbucks desde la fuente autorizada y registrar procedencia y licencia de cada dataset.
2. Instalar el manifiesto consolidado en un entorno limpio y ejecutar los notebooks con dependencia de red/credenciales controlada.
3. Corregir o confirmar con el autor el notebook denominado Prophet que contiene un modelo estructural y revisar la numeración legacy.
4. Normalizar gradualmente el notebook importado de Kaggle al español y documentar los prerrequisitos remotos.
5. Añadir validación de notebooks seleccionados en CI y definir una política de versiones reproducibles.
6. Refactorizar utilidades repetidas después de acordar qué pasos deben permanecer explícitos para el aprendizaje.
