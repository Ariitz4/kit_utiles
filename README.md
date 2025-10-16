# entorno-plantilla_IABD - Plantilla IABD – Entorno y Proyecto Base
Este repositorio es una **plantilla** para prácticas del curso: incluye entorno, estructura de código, tests y notebook de demo.

## 🚀 Arranque rápido

### Opción A: Conda (recomendada)
```bash
conda env create -f environment.yml
conda activate iabd_plantilla
jupyter lab
```

### Opción B: venv + pip
```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```