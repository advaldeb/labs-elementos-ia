# Soluciones: laboratorio 18

## `18_transformer_fundamentals.ipynb`

1. Definir la etiqueta a partir de `X[:, 0]` y usar el embedding del primer token (`encoded[:, 0]`) como representación, en vez de promediar posiciones.
2. Quitar `self.position`, conservar semilla y particiones y volver a entrenar. Si la tarea depende del orden, la validación debería evidenciar qué información perdió el encoder sin posición; interpretar el resultado de la tarea, no asumirlo.
3. Construir `padding_mask` de forma `(batch, seq_len)` con `True` para tokens padding y pasarla como `src_key_padding_mask` al encoder. Comprobar que logits continúan `(batch, n_classes)` para longitudes distintas.