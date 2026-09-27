# Laboratorios de Elementos de Inteligencia Artificial

Material práctico del curso **Elementos de Inteligencia Artificial**, dictado por el profesor **MSc. Abel Valdebenito S.** El repositorio reúne notebooks de Jupyter para estudiar métodos de aprendizaje automático, reducción de dimensionalidad y análisis de series temporales.

## Laboratorios

### 1. Aprendizaje no supervisado

#### Clustering

- [K-means](01%20clustering/01%20kmeans.ipynb)
- [Clustering jerárquico](01%20clustering/02%20hierarchical.ipynb)
- [Mezclas gaussianas (GMM)](01%20clustering/03%20gmmclust.ipynb)

#### Reducción de dimensionalidad

- [Análisis de componentes principales (PCA)](02%20pca%20and%20fa/04%20pca.ipynb)
- [Análisis factorial (FA)](02%20pca%20and%20fa/05%20fa.ipynb)

#### Segmentación de clientes

- [Laboratorio de segmentación de clientes](08%20customer-segmentaion/customer_segmentation.ipynb)

### 2. Aprendizaje supervisado y pronóstico

#### Modelos de regresión

- [Regresión lineal](03%20regression/06%20regression.ipynb)
- [Regresión ridge](03%20regression/07%20regression%20ridge.ipynb)
- [Regresión lasso](03%20regression/08%20regression%20lasso.ipynb)
- [Regresión elastic net](03%20regression/09%20regression%20elasticnet.ipynb)

#### Modelos de regresión basados en árboles

- [Árbol de regresión](04%20treemodels/10%20regressiontree.ipynb)
- [Random forest](04%20treemodels/11%20randomforest.ipynb)
- [Gradient boosting](04%20treemodels/12%20gbm.ipynb)
- [XGBoost](04%20treemodels/13%20xgboost.ipynb)

#### Series temporales

- [Regresiones espurias](06%20time%20series/12%20regespuriats.ipynb)
- [Modelo de rezagos distribuidos](06%20time%20series/13%20distributed%20lag%20model.ipynb)
- [Holt-Winters](06%20time%20series/14%20holt-winters.ipynb)
- [ETS](06%20time%20series/15%20ETS.ipynb)
- [Prophet](06%20time%20series/16%20Prophet.ipynb)

### 3. Deep Learning

### 4. Reinforcement Learning
- TBD

### 4. LLM
- [Curso LLM Engineering](10%20llm-eng/README.md)
- [Configuración del entorno](10%20llm-eng/notebooks/00_setup/00_01_environment_setup.ipynb)
- [Modelos multi-provider](10%20llm-eng/notebooks/00_setup/00_02_multi_provider_llm.ipynb)
- [Tokens y ventana de contexto](10%20llm-eng/notebooks/01_llm_fundamentals/01_01_tokens_and_context.ipynb)
- [Muestreo y generación](10%20llm-eng/notebooks/01_llm_fundamentals/01_02_sampling.ipynb)
- [Fundamentos de prompts](10%20llm-eng/notebooks/02_prompt_engineering/02_01_prompt_basics.ipynb)
- [Zero-shot y few-shot](10%20llm-eng/notebooks/02_prompt_engineering/02_02_zero_shot_few_shot.ipynb)
- [Patrones de prompts e inyección](10%20llm-eng/notebooks/02_prompt_engineering/02_03_prompt_patterns.ipynb)
- [Salidas estructuradas con Pydantic](10%20llm-eng/notebooks/03_structured_outputs/03_01_structured_outputs.ipynb)
- [Validación y reintentos](10%20llm-eng/notebooks/03_structured_outputs/03_02_validation_and_retries.ipynb)
- [Fundamentos de evaluación](10%20llm-eng/notebooks/04_evaluation/04_01_evaluation_basics.ipynb)
- [Evaluación con LLM como juez](10%20llm-eng/notebooks/04_evaluation/04_02_llm_as_judge.ipynb)
- [Comparación de modelos](10%20llm-eng/notebooks/04_evaluation/04_03_model_comparison.ipynb)
- [Representaciones vectoriales y embeddings](10%20llm-eng/notebooks/05_embeddings/05_01_embeddings.ipynb)
- [Búsqueda semántica manual](10%20llm-eng/notebooks/05_embeddings/05_02_semantic_search.ipynb)
- [Chunking y metadatos](10%20llm-eng/notebooks/06_retrieval/06_01_chunking.ipynb)
- [Evaluación de recuperación](10%20llm-eng/notebooks/06_retrieval/06_02_retrieval_evaluation.ipynb)
- [RAG desde cero](10%20llm-eng/notebooks/07_rag/07_01_rag_from_scratch.ipynb)
- [RAG con LangChain](10%20llm-eng/notebooks/07_rag/07_02_rag_langchain.ipynb)
- [Function calling y ejecución de herramientas](10%20llm-eng/notebooks/08_tools/08_01_function_calling.ipynb)
- [Router de herramientas](10%20llm-eng/notebooks/08_tools/08_02_tool_router.ipynb)
- [Agente mínimo desde cero](10%20llm-eng/notebooks/09_agents/09_01_agent_from_scratch.ipynb)
- [Fallos de agentes](10%20llm-eng/notebooks/09_agents/09_02_agent_failures.ipynb)
- [Fundamentos de LangGraph](10%20llm-eng/notebooks/10_langgraph/10_01_langgraph_basics.ipynb)
- [Workflow de agente con LangGraph](10%20llm-eng/notebooks/10_langgraph/10_02_agent_workflow.ipynb)
- [Observabilidad con LangSmith](10%20llm-eng/notebooks/11_observability/11_01_llm_observability.ipynb)
- [Agentic RAG con LangGraph](10%20llm-eng/notebooks/12_advanced_rag/12_01_agentic_rag.ipynb)
- [Capstone: sistema LLM integrado](10%20llm-eng/notebooks/13_capstone/13_01_capstone.ipynb)

### 5. Agentes
- TBD

## Cómo usar este repositorio

1. Abre el repositorio en JupyterLab o Visual Studio Code con soporte para notebooks.
2. Selecciona el laboratorio y ejecuta sus celdas en orden.
3. Si el notebook utiliza datos locales, mantén la estructura de carpetas del repositorio: hay recursos en las subcarpetas `data/` y `code/`.

Los notebooks pueden requerir bibliotecas de Python específicas; revisa sus celdas de importación y las instrucciones incluidas en cada laboratorio antes de ejecutarlos.