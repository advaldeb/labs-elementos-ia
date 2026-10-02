# Soluciones: laboratorios 00–01

## `00_introduction_to_deep_learning.ipynb`

1. Aumentar el ruido eleva la variabilidad de objetivo y normalmente empeora RMSE de train y evaluación. Comparar cada modelo contra el baseline; la magnitud exacta depende de semilla y entrenamiento.
2. Sustituir `Sequential(Linear, Tanh, Linear)` por `Linear(1, 1)`. Solo representa una recta; no puede representar exactamente la curvatura de la función sintética.
3. Ordenar `x` con `np.argsort(x[:, 0])` antes de cortar 70/15/15. Es una evaluación de extrapolación temporal/por rango, más difícil que interpolar muestras mezcladas. No ajustar escala ni parámetros con validación/test.

## `01_tensors_and_autograd.ipynb`

1. Para el componente $i$, aproximar $(L(w_i+h)-L(w_i-h))/(2h)$ con $h$ pequeño y compararlo con `weights.grad[i]`; disminuir `h` hasta que el error de redondeo empiece a crecer.
2. `torch.arange(24).reshape(2, 3, 4)` puede representar dos lotes, tres pasos y cuatro características por paso. Las dimensiones solo adquieren ese significado por la tarea.
3. Después de dos llamadas a `backward()` sin limpiar, los gradientes se suman. `weights.grad = None` o `zero_grad()` entre recorridos restablece la acumulación.