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

### 3. Reinforcement Learning
- TBD

### 4. LLM
- TBD

### 5. Agentes
- TBD

## Cómo usar este repositorio

1. Abre el repositorio en JupyterLab o Visual Studio Code con soporte para notebooks.
2. Selecciona el laboratorio y ejecuta sus celdas en orden.
3. Si el notebook utiliza datos locales, mantén la estructura de carpetas del repositorio: hay recursos en las subcarpetas `data/` y `code/`.

Los notebooks pueden requerir bibliotecas de Python específicas; revisa sus celdas de importación y las instrucciones incluidas en cada laboratorio antes de ejecutarlos.