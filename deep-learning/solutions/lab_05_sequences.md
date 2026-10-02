# Soluciones: laboratorios 15–17

## `15_recurrent_neural_networks.ipynb`

1. Ejecutar la misma secuencia con dos estados iniciales; graficar distancia entre estados ocultos paso a paso. La rapidez de atenuación depende de $W_h$ y tanh.
2. Escalar/modificar `Wh` y graficar estado y norma por paso. Valores grandes pueden llevar saturación o inestabilidad; no hay umbral universal independiente de dimensión.
3. Aplicar una capa de salida a cada estado oculto y definir una pérdida por paso (o solo en pasos objetivo). Alinear máscara con posiciones válidas y evitar evaluar padding.

## `16_lstm_and_gru.ipynb`

1. Para `batch_first=True`, salida es `(batch, seq_len, hidden_size)`; estados LSTM `h_n` y `c_n` son `(num_layers * directions, batch, hidden_size)`.
2. Crear LSTM y GRU con mismas dimensiones; comparar `sum(p.numel() for p in model.parameters())`. LSTM suele tener más parámetros por sus cuatro transformaciones gate frente a tres de GRU.
3. Generar secuencias más largas sin cambiar número de muestras, fijar el resto, cronometrar entrenamiento e informar métrica más duración; repetir si se quiere separar ruido de medición.

## `17_attention_mechanism.ipynb`

1. Con máscara triangular superior, verificar `torch.all(causal_weights[np.triu_indices(seq_len, k=1)] == 0)` y que cada fila válida suma 1.
2. Calcular logits $QK^T$ con y sin división por $\sqrt{d_k}$ para varios tamaños. Sin escala, su varianza crece con dimensión y softmax tiende a concentrarse.
3. La atención es equivariante a permutación de posiciones si se permutan Q/K/V; no conoce orden. Añadir embeddings posicionales aprendidos o sinusoidales y comprobar permutaciones.