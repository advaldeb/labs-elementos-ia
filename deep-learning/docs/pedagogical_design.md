# Decisiones pedagógicas y técnicas

## Progresión

Los primeros laboratorios implementan operaciones pequeñas en NumPy para hacer visibles dimensiones, regla de la cadena y descenso. PyTorch aparece después para automatizar derivadas y construir arquitecturas, no para ocultar el mecanismo central. `forward`, cálculo de pérdida y `zero_grad`, `backward`, `step` permanecen visibles en entrenamiento.

## Evidencia antes de interpretación

Cada notebook avanza de explicación a código, resultado observado e interpretación. Las figuras se adaptan al objeto de estudio: curvas de activación y gradiente, trayectorias de optimización, mapas de características, errores de clasificación o pesos de atención. Las conclusiones numéricas se redactan tras ejecutar las celdas.

## Reproducibilidad y evaluación

Las semillas se fijan cuando existe aleatoriedad. Se usan referencias sencillas y divisiones train/validación/test cuando la tarea lo permite. Validación orienta decisiones; test se reserva para la configuración elegida. Ejemplos exhaustivos de cuatro puntos demuestran un mecanismo, no estiman generalización.

## CPU, descargas y alcance

Las tareas se generan localmente y usan modelos compactos para ejecutarse en CPU. GPU es opcional. No se descargan pesos ni datasets por defecto; transferencia se muestra entre tareas sintéticas. Una ampliación con pesos públicos debe indicar procedencia y licencia y conservar una ruta local equivalente.

## Soluciones

Los notebooks contienen los enunciados, sin respuestas. Las claves docentes se guardan por separado en `solutions/` e identifican módulo y nombre del notebook.