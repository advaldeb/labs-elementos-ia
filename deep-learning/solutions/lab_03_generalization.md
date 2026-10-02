# Soluciones: laboratorios 09–11

## `09_activation_functions.ipynb`

1. En sigmoid, las derivadas pequeñas aparecen en extremos positivos/negativos donde la curva se satura; leer la curva de gradiente, no solo la salida.
2. Restaurar la misma inicialización para GELU y ReLU, variar solo activación y repetir varias semillas. Comparar pérdidas train/validación y dispersión, no una sola corrida.
3. ReLU tiene gradiente cero para entradas negativas; neuronas persistentemente negativas pueden dejar de actualizarse. LeakyReLU mantiene pendiente pequeña y una inicialización coherente ayuda a mantener varianza.

## `10_weight_initialization.ipynb`

1. Mantener arquitectura, datos y semilla; cambiar tanh y comparar distribuciones de activaciones/gradientes. Xavier suele conservar varianza con tanh; Kaiming se deriva para ReLU y puede no ser ideal para tanh.
2. Ejecutar tres semillas por esquema y resumir media y desviación de exactitud junto con las curvas.
3. La pérdida global puede ocultar derivadas casi nulas en capas tempranas o explosivas en otras. Registrar estadísticos por capa de activación y norma de gradiente.

## `11_regularization_and_generalization.ipynb`

1. Tras cada época, copiar el `state_dict` con mejor pérdida/exactitud de validación; restaurarlo antes de evaluar test una vez. No escoger checkpoint mirando test.
2. Variar solo `dropout_rate`, reconstruir modelos desde igual semilla y graficar pérdidas de train y validación. Dropout se desactiva con `model.eval()`.
3. Regularización excesiva restringe el modelo y puede aumentar tanto error train como validación: subajuste. Seleccionar intensidad por validación, no asumir que más es mejor.