# LLM Engineering: de los modelos fundacionales a sistemas de IA en producción

Curso práctico en español sobre diseño, evaluación y operación de sistemas con modelos de lenguaje. El material enseña primero los mecanismos y después introduce abstracciones, con énfasis en fiabilidad, medición, límites de costo y separación de componentes. Las explicaciones, ejemplos, ejercicios y arquitecturas son originales.

## Propósito y enfoque

El objetivo es que puedas construir sistemas LLM cuyo comportamiento se pueda inspeccionar, probar y mejorar, no solo enviar prompts a una API. La secuencia va de tokens y prompts a contratos Pydantic, evaluación, recuperación, RAG, herramientas, agentes, observabilidad y un proyecto integrador.

Los notebooks empiezan con implementaciones pequeñas y visibles: búsqueda vectorial manual antes de LangChain, ciclo de agente manual antes de LangGraph y evaluaciones locales antes de conectar proveedores. Cada práctica propone experimentos, registra métricas en DataFrames y discute límites de los resultados.

## Itinerario del curso

### 00. Entorno y modelos

- [00.1 Preparación del entorno](notebooks/00_setup/00_01_environment_setup.ipynb)
- [00.2 Acceso multi-proveedor](notebooks/00_setup/00_02_multi_provider_llm.ipynb)

Se instala el entorno, se valida la configuración y se presenta `get_llm` para alternar modelos locales Ollama y modelos OpenAI o Anthropic sin reescribir la aplicación.

### 01. Fundamentos de modelos de lenguaje

- [01.1 Tokens y ventana de contexto](notebooks/01_llm_fundamentals/01_01_tokens_and_context.ipynb)
- [01.2 Muestreo y generación](notebooks/01_llm_fundamentals/01_02_sampling.ipynb)

Tokens, presupuesto de contexto, logits, temperatura, top-p y variación de generación.

### 02. Ingeniería de prompts

- [02.1 Fundamentos de prompts](notebooks/02_prompt_engineering/02_01_prompt_basics.ipynb)
- [02.2 Zero-shot y few-shot](notebooks/02_prompt_engineering/02_02_zero_shot_few_shot.ipynb)
- [02.3 Patrones e inyección de prompts](notebooks/02_prompt_engineering/02_03_prompt_patterns.ipynb)

Instrucciones versionadas, ejemplos, evaluación controlada y manejo de contenido externo no confiable.

### 03. Salidas estructuradas

- [03.1 Contratos con Pydantic](notebooks/03_structured_outputs/03_01_structured_outputs.ipynb)
- [03.2 Validación y reintentos](notebooks/03_structured_outputs/03_02_validation_and_retries.ipynb)

`BaseModel`, `Field`, `Enum`, campos opcionales, esquemas anidados, validadores, errores, serialización, JSON Schema y recuperación acotada.

### 04. Evaluación

- [04.1 Métricas básicas y similitud semántica](notebooks/04_evaluation/04_01_evaluation_basics.ipynb)
- [04.2 Evaluación con LLM como juez](notebooks/04_evaluation/04_02_llm_as_judge.ipynb)
- [04.3 Comparación de modelos](notebooks/04_evaluation/04_03_model_comparison.ipynb)

Exact match, accuracy, cumplimiento de esquema, similitud coseno de embeddings, rúbricas, latencia, uso de tokens, fallos y comparación controlada.

### 05. Embeddings

- [05.1 Representaciones vectoriales](notebooks/05_embeddings/05_01_embeddings.ipynb)
- [05.2 Búsqueda semántica manual](notebooks/05_embeddings/05_02_semantic_search.ipynb)

Vectores, TF-IDF, SVD, cosine similarity y nearest neighbors. Las representaciones de juguete se distinguen de embeddings neuronales preentrenados.

### 06. Recuperación

- [06.1 Chunking y metadatos](notebooks/06_retrieval/06_01_chunking.ipynb)
- [06.2 Evaluación de recuperación](notebooks/06_retrieval/06_02_retrieval_evaluation.ipynb)

Fragmentación, solapamiento, trazabilidad y métricas Hit Rate@K, Precision@K, Recall@K y MRR.

### 07. Generación aumentada por recuperación

- [07.1 RAG desde cero](notebooks/07_rag/07_01_rag_from_scratch.ipynb)
- [07.2 RAG con LangChain](notebooks/07_rag/07_02_rag_langchain.ipynb)

Se mide retrieval independientemente de generación, se preservan fuentes y se trata el contenido recuperado como no confiable.

### 08. Herramientas

- [08.1 Function calling y ejecución](notebooks/08_tools/08_01_function_calling.ipynb)
- [08.2 Router de herramientas](notebooks/08_tools/08_02_tool_router.ipynb)

Contratos Pydantic para calculadora, clima de ejemplo, catálogo local y búsqueda documental; selección y ejecución son etapas distintas.

### 09. Agentes

- [09.1 Agente mínimo desde cero](notebooks/09_agents/09_01_agent_from_scratch.ipynb)
- [09.2 Fallos y salvaguardas](notebooks/09_agents/09_02_agent_failures.ipynb)

Ciclo observar-decidir-ejecutar, límites de pasos y llamadas, herramientas inventadas, argumentos inválidos, repeticiones y crecimiento del contexto.

### 10. LangGraph

- [10.1 Estado, nodos, rutas y persistencia](notebooks/10_langgraph/10_01_langgraph_basics.ipynb)
- [10.2 Workflow de agente](notebooks/10_langgraph/10_02_agent_workflow.ipynb)

StateGraph, nodos, bordes, routing condicional, checkpoint e interrupción para revisión humana.

### 11. Observabilidad

- [11.1 Trazas y evaluación con LangSmith](notebooks/11_observability/11_01_llm_observability.ipynb)

Instrumenta el workflow RAG previo. LangSmith es optativo; la práctica local funciona sin credenciales y enseña trazas, runs, datasets, experimentos, evaluadores y análisis de errores.

### 12. RAG avanzado

- [12.1 Agentic RAG con LangGraph](notebooks/12_advanced_rag/12_01_agentic_rag.ipynb)

Router, reescritura de consulta, retriever, grader, decisión de contexto, reintentos limitados, generación opcional, validación y abstención.

### 13. Proyecto integrador

- [13.1 Sistema LLM completo](notebooks/13_capstone/13_01_capstone.ipynb)

Integra modelos configurables, Pydantic, prompts, retrieval, RAG, herramientas, LangChain, LangGraph, evaluación y LangSmith opcional. Prepara la comparación de Ollama y OpenAI con un máximo de dos llamadas y métricas de calidad, retrieval, seguimiento, esquema, latencia, tokens, costo y fallos.

## Arquitectura y datos

- `config/models.yaml`: proveedores y nombres de modelo configurables.
- `config/settings.yaml`: parámetros generales del curso.
- `config/pricing.yaml`: tarifas USD por millón de tokens. Se dejan vacías hasta registrar valores vigentes con fuente y fecha; sin tarifa o metadatos de tokens, el costo se informa como desconocido.
- `src/llm_engineering/models/`: fábrica común `get_llm(provider, model, temperature, ...)` y contratos de configuración.
- `src/llm_engineering/schemas/`, `prompts/`, `retrieval/`, `tools/`, `agents/`, `evaluation/` y `observability/`: componentes reutilizables separados por responsabilidad.
- `data/documents/faq.jsonl`: corpus sintético compartido por los ejemplos de recuperación.
- `data/outputs/`: resultados del capstone; las prácticas anteriores mantienen sus CSV existentes en `outputs/`.

## Requisitos e instalación

Se requiere Python 3.11 o posterior y JupyterLab o Visual Studio Code con la extensión Jupyter. Ollama es opcional para modelos locales. OpenAI y Anthropic requieren sus respectivas credenciales para las prácticas remotas.

En Windows PowerShell, desde la raíz del repositorio:

```powershell
Set-Location "10 llm-eng"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
Copy-Item .env.example .env
jupyter lab
```

Abre los notebooks desde `10 llm-eng/notebooks/` y ejecuta sus celdas en orden. `requirements.txt` permite instalación directa; la instalación editable recomendada también registra el paquete local.

## Proveedores, seguridad y costos

Los nombres de modelo se cambian mediante `config/models.yaml` o las variables `OLLAMA_MODEL`, `OPENAI_MODEL` y `ANTHROPIC_MODEL`. No hay claves en el código: usa `.env` local, no lo publiques y nunca imprimas sus valores.

Las llamadas remotas y la publicación a LangSmith están desactivadas por defecto. Revisa número máximo de solicitudes, costo potencial y datos transmitidos antes de habilitar una práctica; retrieved content se trata como no confiable. LangSmith puede almacenar entradas y salidas, así que actívalo solo con consentimiento y configuración explícita.

## Reproducibilidad y pruebas

Los experimentos registran configuración, versión de prompt y parámetros cuando corresponde. Se fijan semillas para simulaciones locales; las generaciones remotas son probabilísticas y pueden cambiar entre ejecuciones o versiones de modelo. Los resultados se organizan en pandas DataFrames y se guardan en CSV.

Desde esta carpeta, ejecuta:

```powershell
python -m pytest
```

Las pruebas usan herramientas y modelos simulados para verificar contratos, routing y workflows sin credenciales ni consumo de API.