# Catálogo de datasets

El inventario, variables observables, rutas, usos, procedencia conocida y limitaciones se mantiene en [data/README.md](../data/README.md). Los notebooks deben resolver rutas con `ml_course.data.get_data_path` y no depender del directorio de trabajo.

Los recursos de entrada viven en `data/raw/` o `data/external/`; los resultados derivados futuros corresponden a `data/processed/`. Los datasets originales no deben sobrescribirse. Los archivos ZIP legacy se conservan sin extracción automática.
