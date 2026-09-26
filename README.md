# Laboratorios de Elementos de Inteligencia Artificial

Material práctico del curso **Elementos de Inteligencia Artificial**, dictado por el profesor **MSc. Abel Valdebenito S.** El repositorio reúne notebooks de Jupyter para estudiar métodos de aprendizaje automático, reducción de dimensionalidad y análisis de series temporales.

## Laboratorios

### Aprendizaje no supervisado

- [K-means](01%20clustering/01%20kmeans.ipynb), [clustering jerárquico](01%20clustering/02%20hierarchical.ipynb) y [mezclas gaussianas (GMM)](01%20clustering/03%20gmmclust.ipynb).
- [Análisis de componentes principales (PCA)](02%20pca%20and%20fa/04%20pca.ipynb) y [análisis factorial (FA)](02%20pca%20and%20fa/05%20fa.ipynb).
- [Segmentación de clientes](08%20customer-segmentaion/customer_segmentation.ipynb).

### Aprendizaje supervisado y pronóstico

- [Regresión lineal](03%20regression/06%20regression.ipynb), [ridge](03%20regression/07%20regression%20ridge.ipynb), [lasso](03%20regression/08%20regression%20lasso.ipynb) y [elastic net](03%20regression/09%20regression%20elasticnet.ipynb).
- [Árbol de regresión](04%20treemodels/10%20regressiontree.ipynb), [random forest](04%20treemodels/11%20randomforest.ipynb), [gradient boosting](04%20treemodels/12%20gbm.ipynb) y [XGBoost](04%20treemodels/13%20xgboost.ipynb).
- Series temporales: [regresiones espurias](06%20time%20series/12%20regespuriats.ipynb), [rezagos distribuidos](06%20time%20series/13%20distributed%20lag%20model.ipynb), [Holt-Winters](06%20time%20series/14%20holt-winters.ipynb), [ETS](06%20time%20series/15%20ETS.ipynb) y [Prophet](06%20time%20series/16%20Prophet.ipynb).

## Cómo usar este repositorio

1. Abre el repositorio en JupyterLab o Visual Studio Code con soporte para notebooks.
2. Selecciona el laboratorio y ejecuta sus celdas en orden.
3. Si el notebook utiliza datos locales, mantén la estructura de carpetas del repositorio: hay recursos en las subcarpetas `data/` y `code/`.

Los notebooks pueden requerir bibliotecas de Python específicas; revisa sus celdas de importación y las instrucciones incluidas en cada laboratorio antes de ejecutarlos.