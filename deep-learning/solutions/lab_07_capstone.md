# Soluciones: laboratorio 19

## `19_deep_learning_capstone.ipynb`

1. Limitar el muestreo de índices de entrenamiento a 20 por clase, sin tocar `val_idx` ni `test_idx`. Mantener el mismo pipeline y comparar las dos curvas; se espera mayor variabilidad con menos ejemplos, pero medirlo.
2. Aplicar `torch.rot90` o `affine_grid/grid_sample` solo a batches de train. Para una rotación continua pequeña, mantener etiquetas y usar la misma semilla. Comparar matrices de confusión y ejemplos en validación.
3. Repetir división y entrenamiento para al menos cinco semillas; guardar únicamente métricas de validación para selección y reportar media/desviación por arquitectura. Una vez fijado el protocolo, reentrenar configuración elegida y consultar test al final.