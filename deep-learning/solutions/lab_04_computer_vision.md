# Soluciones: laboratorios 12–14

## `12_convolutions.ipynb`

1. Intercambiar el kernel vertical por su transpuesto. El filtro responde ante transiciones horizontales; verificar imagen, kernel y salida.
2. Con padding $p=1$, kernel 3, stride 1 y entrada 7×7, la salida vuelve a 7×7: $\lfloor (7+2p-3)/1\rfloor+1$.
3. Comparar en una cuadrícula de stride y padding, cambiando una variable a la vez. Reportar forma de salida y mapa; padding modifica bordes y stride el muestreo.

## `13_convolutional_neural_networks.ipynb`

1. Encontrar `wrong = (test_predictions != y[test_idx]).nonzero()`, mostrar imagen, etiqueta real y predicción. Si no hay errores, informar que el conjunto sintético no ofrece caso erróneo y mostrar aciertos con mayor incertidumbre.
2. Alterar solo número de canales/filtros, fijar semilla y número de épocas, seleccionar con validación y comparar desempeño/coste.
3. Aplicar la misma distribución de transformaciones a train solamente (o reproducir aumento en cada época); no transformar validación/test. Rotaciones y traslaciones moderadas pueden mejorar invariancia, pero también alterar etiquetas.

## `14_transfer_learning.ipynb`

1. Imprimir `[(name, parameter.requires_grad) ...]` antes y después de congelar `features`; la cabeza nueva debe permanecer entrenable.
2. Comparar extractor preentrenado local (tarea fuente sintética) con extractor congelado aleatorio bajo mismos datos y split. Si se inicializa al azar, fijar semilla y verificar que el experimento realmente lo reemplace.
3. Descongelar solo el último bloque y usar una tasa menor para extractor que para cabeza; elegir por validación con el mismo presupuesto. Mantener test intacto.