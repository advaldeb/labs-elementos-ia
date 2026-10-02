# Soluciones: laboratorios 20–22

## `20_tabular_embeddings_churn.ipynb`

1. Cambiar solo el último valor de `embedding_dims` (1 y 16) y reentrenar con la misma semilla. Comparar AUC de validación y la correlación de la proyección con `branch_risk`. Con dimensión 1 el embedding puede representar el riesgo latente (es un escalar); con 16 hay más parámetros que información por sucursal y la validación decide si se sobreajusta. Esperar diferencias pequeñas y reportarlas con su semilla.
2. Calcular `pos_weight = (1 - tasa) / tasa` con la tasa de train y pasarlo como tensor a `binary_cross_entropy_with_logits`. La *log loss* de validación empeora porque las probabilidades quedan sesgadas hacia arriba (descalibradas); la precisión en el 10 % superior cambia poco, porque depende del orden de los puntajes y no de su escala. Conclusión: ponderar clases es una decisión de calibración, no de ranking.
3. Dentro del ciclo de entrenamiento, antes del `forward`, clonar `x_cat` y aplicar `mask = torch.rand(len(x_cat), device=device) < 0.05; x_cat[mask, 3] = 0`. Así la fila 0 recibe gradiente y aprende algo parecido a una sucursal promedio. Repetir la prueba de sucursal desconocida: la caída de AUC y el desplazamiento de la probabilidad media deberían reducirse respecto del modelo original. Discutir el costo: el modelo pierde un poco de información en train.

## `21_neural_recommender.ipynb`

1. Pasar `n_negatives=1` y `n_negatives=10` a `train_recommender` para MF. Con pocos negativos el modelo ve menos contraste y puede sobrestimar productos populares; con muchos, cada época es más lenta (el tiempo crece casi linealmente con el número de filas). Reportar NDCG@10 de validación y segundos por época.
2. Iterar `for dim in (2, 4, 8, 16, 32)` entrenando `MatrixFactorization(n_users, n_items, dim)`. El generador usa 4 factores latentes: se espera un máximo cerca de dimensiones pequeñas y estabilidad o leve deterioro al crecer, porque los datos por usuario son escasos. La curva se elige en validación; test solo para la dimensión final.
3. Elegir dos productos de una misma categoría, crear `new_user = torch.zeros(1, d, requires_grad=True)` y optimizar con Adam solo ese vector, usando los embeddings y sesgos de producto de MF congelados (`with torch.no_grad()` para los pesos o `requires_grad_(False)`), con los dos positivos y negativos muestreados. Puntuar con `new_user @ item_embedding.weight.T + item_bias.weight.T`. El top 10 debería concentrarse en la categoría de los productos de entrada, a diferencia de la lista de popularidad, que es igual para todos.

## `22_time_series_forecasting.ipynb`

1. Crear copias de `data[split]` con el tensor `future` en ceros (`torch.zeros_like`) para train, validación y test, y reentrenar la arquitectura elegida. El MAE en días con promoción debería aumentar claramente y acercarse al de los baselines; el de días sin promoción cambia menos. Esto muestra que la ganancia proviene del dato de promociones planificadas.
2. Cambiar `LOOKBACK` y volver a ejecutar desde la celda de ventanas (las capas dependen de `LOOKBACK`). Con 14 días se pierde contexto estacional; con 56 aumentan parámetros de MLP y CNN y el tiempo de la LSTM. Reportar WAPE de validación y tiempo por arquitectura en una tabla.
3. Reemplazar `F.l1_loss` por la pérdida pinball: `e = target - prediction; loss = torch.maximum(q * e, (q - 1) * e).mean()` con `q = 0.9`. En test, calcular `(y_test_units <= forecast_p90).mean()`; un valor cercano a 0,9 indica buena calibración. El P90 menos el pronóstico mediano aproxima un stock de seguridad; discutir el costo de quiebre frente al costo de inventario.
