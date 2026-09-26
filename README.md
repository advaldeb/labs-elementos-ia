# Laboratorios de Elementos de Inteligencia Artificial

Repositorio de apoyo para el curso **Elementos de Inteligencia Artificial**, dictado por el profesor **MSc. Abel Valdebenito S.** Aquí se reúnen notebooks y archivos de datos para explorar métodos de aprendizaje automático y análisis de datos mediante ejercicios prácticos.

## Contenidos

- **Clustering:** K-means, clustering jerárquico y modelos de mezclas gaussianas (GMM).
- **Reducción de dimensionalidad:** análisis de componentes principales (PCA) y análisis factorial (FA).
- **Regresión:** regresión lineal, ridge, lasso y elastic net.
- **Modelos de árboles:** árboles de regresión, random forest, gradient boosting y XGBoost.
- **Series temporales:** regresiones espurias, modelos de rezagos distribuidos, Holt-Winters, ETS y Prophet.
- **Segmentación de clientes:** análisis de perfiles y portafolios de clientes.

## Organización

Los materiales están agrupados por tema en carpetas numeradas. Cada notebook contiene el desarrollo de un laboratorio y, cuando corresponde, los archivos de datos asociados:

| Carpeta | Tema |
| --- | --- |
| `01 clustering/` | Métodos de clustering |
| `02 pca and fa/` | PCA y análisis factorial |
| `03 regression/` | Modelos de regresión y pronóstico |
| `04 treemodels/` | Modelos basados en árboles |
| `06 time series/` | Análisis y pronóstico de series temporales |
| `08 customer-segmentaion/` | Segmentación de clientes |

Los notebooks están en formato Jupyter (`.ipynb`). Para ejecutarlos, abre el repositorio en JupyterLab o Visual Studio Code con soporte para notebooks y asegúrate de instalar las bibliotecas que cada laboratorio importa. Algunos ejercicios requieren los archivos ubicados en las subcarpetas `data/` o `code/`; conserva la estructura de directorios para que sus rutas funcionen.