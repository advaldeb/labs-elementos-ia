# Soluciones: laboratorios 02–05

## `02_neuron_and_perceptron.ipynb`

1. Para ejemplo $x$, etiqueta $y$ y predicción binaria $\hat y$, usar $e=y-\hat y$, `w += rate * e * x` y `b += rate * e`. Sustituir la fila del ejercicio y mostrar los parámetros antes/después.
2. Reordenar con una permutación fija y entrenar hasta cero errores, contando épocas. El orden puede cambiar la trayectoria y número de pasadas, no la separabilidad de AND.
3. Añadir la característica $x_1x_2$ permite separar XOR en el espacio extendido; las cuatro filas pasan a ser `[x1, x2, x1*x2]`. Esto anticipa una transformación aprendida por una capa oculta.

## `03_multilayer_perceptron_numpy.ipynb`

1. Reiniciar `rng = np.random.default_rng(SEED)`, cambiar `hidden_units = 2` y reconstruir pesos con las formas correspondientes. Entrenar de nuevo y verificar las cuatro predicciones, no reutilizar pesos de tamaño anterior.
2. Reemplazar `tanh(z)` por `maximum(z, 0)` y su derivada por `(z > 0)`. Propagar `d_hidden = d_logits @ W2.T`; luego `d_z1 = d_hidden * (z1 > 0)` y calcular `dW1`, `db1` como en el notebook.
3. Perturbar un solo `W1[i, j]` en $+h$ y $-h$, recalcular BCE sin actualizar pesos y contrastar la diferencia central con `dW1[i, j]`. En `float32`, comenzar con `h=1e-3` y reportar error absoluto/relativo.

## `04_forward_propagation.ipynb`

1. Modificar el mismo elemento de `W2` en NumPy y `layer2.weight` en PyTorch (recordar que `nn.Linear` almacena `(out_features, in_features)`). Comparar `np.allclose`.
2. Para tercera capa con tamaños $d_1,d_2,d_3$, usar `W1:(d_in,d1)`, `W2:(d1,d2)`, `W3:(d2,d3)` en NumPy. Las capas lineales PyTorch esperan transpuestas.
3. Una conexión residual exige que la entrada y la salida sumada tengan igual forma. Si las dimensiones difieren, proyectar la entrada con una capa lineal antes de sumar.

## `05_backpropagation.ipynb`

1. Cambiar `target_one`, reconstruir hojas y recalcular ambos caminos desde parámetros nuevos. Los gradientes deben coincidir numéricamente; la dirección puede no ser la misma para todos los parámetros si se cambia la posición relativa del objetivo.
2. Guardar `model[0].weight.grad.norm().item()` después de `backward()` y antes del `step()` por época. Graficarlo en eje propio o escala log junto con pérdida; picos/casi ceros requieren inspeccionar inicialización, activaciones y tasa.
3. Registrar normas por profundidad en redes con 2 y 6 capas usando igual entrada, inicialización y activación. No hay respuesta universal: tanh saturado puede atenuar; pesos/tasas grandes pueden amplificar.