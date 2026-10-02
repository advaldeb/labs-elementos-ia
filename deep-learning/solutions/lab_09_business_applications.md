# Soluciones: laboratorios 23–26

## `23_image_quality_inspection.ipynb`

1. Cambiar `COST_FN` y volver a ejecutar la celda del umbral. Con `COST_FN=10` el umbral sube (rechazar piezas buenas pesa relativamente más) y se rechazan menos piezas; con `COST_FN=200` baja y aumentan los falsos positivos. El modelo no cambia: solo la regla de decisión.
2. Calcular `counts = np.bincount(labels[train_idx])`, `weights = torch.tensor(counts.sum() / (3 * counts), dtype=torch.float32, device=device)` y pasar `weight=weights` a `F.cross_entropy` en el entrenamiento (no en la validación usada para *early stopping*, o documentar el cambio). Se espera mayor *recall* de defectos y más falsos positivos; comparar el costo con el umbral reoptimizado en validación.
3. Usar `train_idx = train_idx[:300]` antes de construir `splits`, sin tocar `val_idx` ni `test_idx`. Con pocos datos, el aumento de datos multiplica las vistas de cada defecto en distintas orientaciones; se espera una brecha mayor a favor de `cnn_aumento`. Repetir con al menos tres semillas antes de concluir.

## `24_autoencoder_anomaly_detection.ipynb`

1. Ejecutar `train_autoencoder(bottleneck=2)` y `train_autoencoder(bottleneck=10)`. Con 10 dimensiones para 14 variables, el modelo puede aproximar la identidad y reconstruir también las anomalías, con menor MSE de validación pero peor precisión promedio. Con 2 puede no capturar bien el comportamiento normal. El MSE de validación no es el criterio de detección.
2. Filtrar `clean_train = train_idx[is_anomaly[train_idx] == 0]` y entrenar con `X_t['train'] = torch.tensor(X[clean_train], ...)`. Suele mejorar la separación, porque el modelo no aprende a reconstruir anomalías. Discutir que en la práctica solo se puede filtrar lo ya confirmado: es un escenario optimista.
3. Generar transacciones con `category=2`, `hour≈9` y monto alto, aplicar la misma estandarización (con medias de train) y obtener sus puntajes con cada método sin reentrenar. Calcular su percentil dentro de test. Para monitorear, registrar la distribución del puntaje y el volumen de alertas por día, y revisar una muestra de casos de puntaje medio, no solo los de mayor puntaje.

## `25_text_ticket_classification.ipynb`

1. En `encode_bag`, usar solo `unigrams`, reconstruir `bag_data` y reentrenar. Evaluar en el subconjunto `[i for i in val_idx if 'no es un problema de' in masked[i]]`. Con plantillas como estas, la diferencia puede ser pequeña porque las palabras del problema real dominan; reportarla con su tamaño de muestra.
2. Cambiar `add_typos(..., p=0.15)` y ejecutar desde la generación de datos. Aumentan los tokens desconocidos y caen las reglas y ambos modelos. Propuesta: tokenizar con n-gramas de caracteres o subpalabras (como en el laboratorio 26), que comparten información entre "problema" y "prblema".
3. Optimizar un escalar `T` (por ejemplo, `log_T` con `requires_grad=True` y Adam) minimizando la entropía cruzada de `logits / T` en validación con el modelo congelado. Recalcular la curva de cobertura y el umbral con las probabilidades calibradas y verificar si la exactitud automática en test queda más cerca de 97 %.

## `26_siamese_entity_resolution.ipynb`

1. En `build_pairs`, eliminar el bucle de negativos difíciles y mantener solo el aleatorio. El modelo aprende que compartir apellido basta para unir y la precisión en test (que sí contiene homónimos y hermanos) cae. Conclusión: el conjunto de entrenamiento debe contener los casos difíciles que aparecerán en producción.
2. Quitar `'email'` de `FIELDS` y ejecutar desde la celda de trigramas. Se espera que caiga sobre todo la precisión (el correo distingue homónimos) y algo el *recall* (cuando coincide, es evidencia fuerte). Repetir con otros campos para ordenar su aporte.
3. Elegir el menor umbral con precisión de validación ≥ 0,99: `min(t for t in grid if pair_metrics(y, (s >= t).astype(int))['precision'] >= 0.99)`. Repetir la agrupación: se estiman más clientes únicos (quedan duplicados sin fusionar) y menos grupos mezclados. Un duplicado no fusionado cuesta comunicaciones repetidas y métricas infladas; una fusión errónea mezcla datos personales de dos personas, un riesgo legal y reputacional mayor.
