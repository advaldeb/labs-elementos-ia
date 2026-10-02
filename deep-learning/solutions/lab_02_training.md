# Soluciones: laboratorios 06–08

## `06_loss_functions.ipynb`

1. Modificar una sola predicción y recalcular `abs(error).mean()` y `error.square().mean()`. MSE cambia más cuando se agranda un error aislado.
2. Crear logits como `[[-8.0, 8.0]]` con clase correcta 0. `CrossEntropyLoss` devuelve pérdida alta porque el modelo asigna casi toda la probabilidad a la clase errónea; `argmax` solo informa acierto/error.
3. MAE o Huber reducen influencia de errores extremos respecto de MSE. Complementar con RMSE/MAE y análisis de residuos; la decisión depende del coste del error.

## `07_gradient_descent.ipynb`

1. Usar $L(\theta)=(\theta+2)^2$ y $dL/d\theta=2(\theta+2)$; la actualización debe acercarse a $-2$ para una tasa estable.
2. Mantener inicio, función y tasa; correr 10 y 100 pasos. Registrar parámetros y pérdidas para separar velocidad inicial de convergencia.
3. Usar $L(x,y)=100x^2+y^2$. La curvatura difiere cien veces; una tasa buena para el eje empinado puede hacer lentísimo el eje suave o volver inestable el empinado. Visualizar contornos y trayectoria.

## `08_optimizers_and_training_loop.ipynb`

1. Cambiar solo el learning rate común; reconstruir cada optimizador y restaurar exactamente el mismo `state_dict` inicial antes de entrenar.
2. Alterar únicamente la tasa de Adam y registrar la pérdida final y curvas completas; no inferir superioridad a partir de una tasa aislada.
3. Definir una pequeña grilla antes de mirar test, ajustar cada combinación en train, elegir por validación, congelar el modelo y evaluar test una única vez.