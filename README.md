# Laboratorios de Elementos de IA

Repositorio de apoyo para cursos prácticos de Inteligencia Artificial. El material actual se organiza en tres itinerarios: **Machine Learning**, **Deep Learning** e **Ingeniería de sistemas con modelos de lenguaje (LLM Engineering)**. Las explicaciones docentes están principalmente en español; archivos, módulos y nombres de código usan inglés.

## Cursos

### Machine Learning

[Abrir el curso](machine_learning/README.md) · [Ruta de aprendizaje](machine_learning/docs/learning_path.md) · [Catálogo de datos](machine_learning/docs/datasets.md)

El curso trabaja análisis no supervisado, reducción de dimensionalidad, modelos predictivos y series temporales con notebooks de Jupyter:

- **Clustering:** K-Means, agrupamiento jerárquico y mezclas gaussianas.
- **Reducción de dimensionalidad:** PCA y análisis factorial.
- **Modelos lineales:** regresión lineal, Ridge, Lasso y Elastic Net.
- **Árboles y ensembles:** árboles de regresión, random forest, gradient boosting y XGBoost.
- **Series temporales:** regresiones espurias, modelos de rezagos distribuidos, Holt-Winters, ETS, Prophet, SARIMA y un notebook histórico de modelos estructurales.
- **Segmentación de clientes:** análisis de perfiles y agrupamiento.
- **Clasificación y selección de modelos:** carpetas preparadas para material futuro; todavía no contienen laboratorios implementados.

La mayoría de los datos se centraliza en `machine_learning/data/`. Algunos recursos históricos están incompletos o faltan: el notebook de segmentación requiere un transcript que no está en el repositorio, y los ZIP legacy preservados están vacíos. Consulta el [informe de reorganización](REORGANIZATION_REPORT.md) antes de asumir que todos los notebooks pueden ejecutarse sin ajustes.

### Deep Learning

[Abrir el curso](deep-learning/README.md)

Veinte laboratorios progresan desde tensores, neuronas y una implementación MLP con NumPy hasta entrenamiento con PyTorch, regularización, visión por computador, redes recurrentes, atención y Transformers. El cierre integra comparación de modelos y análisis de errores.

Los experimentos generan datos sintéticos localmente, fijan semillas y no requieren credenciales, pesos preentrenados ni descargas. Están diseñados para CPU; GPU es opcional. Cada notebook incluye ejercicios guiados, independientes y de desafío. Las claves docentes están separadas en `deep-learning/solutions/`.

### LLM Engineering

[Abrir el curso](llm-engineering/README.md)

El itinerario abarca configuración de modelos, tokens y generación, ingeniería de prompts, salidas estructuradas con Pydantic, evaluación, embeddings, búsqueda semántica, recuperación, RAG, herramientas, agentes, LangGraph, observabilidad, RAG avanzado y un proyecto integrador.

La mayoría de las prácticas puede trabajarse localmente con datos de ejemplo. La conexión con Ollama es opcional; los proveedores OpenAI y Anthropic requieren credenciales propias, y LangSmith es opcional. Las llamadas externas están sujetas a disponibilidad, costo y configuración.

## Estructura principal

```text
machine_learning/   Curso de ML, datos, documentación, código y pruebas
deep-learning/      20 laboratorios de redes neuronales y soluciones docentes
llm-engineering/    Curso independiente de LLM, paquete, configuración y pruebas
01 clustering/      Directorio histórico vacío
03 regression/      Directorio histórico vacío
06 time series/     Directorio histórico vacío
notebooks/          Material histórico organizado parcialmente por tema
LICENSE
REORGANIZATION_REPORT.md
```

Las rutas canónicas para el material mantenido son las indicadas en cada curso; los directorios históricos de la raíz no sustituyen esos subproyectos.

## Instalación

Se recomienda Python **3.11 o 3.12**. Cada curso mantiene sus propios manifiestos y puede requerir versiones o proveedores distintos; para evitar conflictos, crea un entorno virtual por subproyecto. Desde la raíz, para Machine Learning:

```powershell
py -3.12 -m venv .venv-ml
.venv-ml\Scripts\Activate.ps1
python -m pip install --upgrade pip
Set-Location machine_learning
python -m pip install -r requirements.txt
```

Para Deep Learning, crea otro entorno virtual, actívalo y ejecuta desde la raíz:

```powershell
py -3.12 -m venv .venv-dl
.venv-dl\Scripts\Activate.ps1
python -m pip install -r deep-learning/requirements.txt
```

Para LLM Engineering, crea un tercer entorno, actívalo y ejecuta la instalación editable desde su carpeta:

```powershell
py -3.12 -m venv .venv-llm
.venv-llm\Scripts\Activate.ps1
Set-Location llm-engineering
python -m pip install -e "[dev]"
```

En macOS o Linux, activa el entorno con `source .venv/bin/activate`. Deep Learning también puede instalarse como proyecto editable con `python -m pip install -e "deep-learning[dev]"`.

## Ejecución y validación

Abre la raíz del repositorio en VS Code/Jupyter y selecciona el kernel del entorno correspondiente al curso. Ejecuta las celdas de cada notebook en orden. Los requisitos y las instrucciones específicas están en los README de [Machine Learning](machine_learning/README.md), [Deep Learning](deep-learning/README.md) y [LLM Engineering](llm-engineering/README.md).

Pruebas disponibles:

```powershell
python -m pytest machine_learning/tests
python -m pytest deep-learning/tests
python -m pytest llm-engineering/tests
```

Ejecuta cada comando desde la raíz, con el entorno que tenga instaladas las dependencias de ese subproyecto.

## Datos, credenciales y pesos

- Machine Learning documenta sus datasets y limitaciones en [machine_learning/docs/datasets.md](machine_learning/docs/datasets.md). No des por disponibles los recursos legacy o externos sin revisar el catálogo.
- Deep Learning genera ejemplos pequeños localmente; no incluye pesos ni datasets grandes.
- LLM Engineering conserva el corpus sintético dentro de su subproyecto. Mantén las credenciales en un `.env` local a partir de `.env.example`; nunca publiques claves. Revisa los límites de costo y los datos enviados antes de activar proveedores remotos o trazas.
- Los datasets grandes, secretos y pesos descargados no deben añadirse al control de versiones.

## Convenciones

- El material docente y sus interpretaciones se redactan en español; nombres de archivos, APIs y código permanecen en inglés.
- Mantén visibles los mecanismos que se enseñan; extrae utilidades solo cuando la reutilización no oculte el aprendizaje.
- Separa entrenamiento, validación y prueba cuando corresponda; reserva test para la evaluación final.
- No inventes métricas: las conclusiones deben corresponder a salidas obtenidas al ejecutar los experimentos.

## Licencia

Consulta [LICENSE](LICENSE). Revisa además las licencias y procedencia de los datasets o servicios de terceros antes de redistribuir sus contenidos.
