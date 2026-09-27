# Configuración del entorno

## Requisitos

Se recomienda Python 3.11 o 3.12. El proyecto requiere Python 3.10 o posterior. Prophet y pmdarima instalan componentes nativos en algunas plataformas; si la instalación falla, usa un entorno compatible de Conda o revisa la documentación oficial de esos paquetes.

## Instalación desde la raíz

En PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

En macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

El manifiesto raíz instala el paquete docente en modo editable, sus dependencias directas y pytest. Para registrar el kernel en Jupyter, ejecuta `python -m ipykernel install --user --name ml-course --display-name "Python (ML Course)"` desde el entorno.

## Selección de kernel

Abre la carpeta raíz en JupyterLab o Visual Studio Code y selecciona el kernel `Python (ML Course)` o el intérprete `.venv`. Ejecuta cada notebook desde la primera celda. Los loaders del paquete `ml_course` descubren la raíz del repositorio a partir de su ubicación instalada.

## Subproyecto LLM Engineering

`10 llm-eng/` conserva su configuración de paquete y sus manifiestos propios. El manifiesto raíz incluye sus dependencias directas para ofrecer una instalación unificada. Para trabajar solo en ese curso se puede crear un entorno separado e instalar `10 llm-eng/requirements.txt` desde esa carpeta.

Algunos laboratorios LLM necesitan un proveedor remoto o un servicio local. Copia `.env.example` a `.env` y configura únicamente las variables pertinentes. Nunca agregues secretos a Git.

## Pruebas

Desde la raíz, ejecuta `python -m pytest`. Las pruebas cubren utilidades reutilizables; los notebooks no tienen pruebas unitarias convencionales en esta fase.
