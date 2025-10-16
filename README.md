# Kit de Utilidades – Proyecto Python

Este proyecto es un **kit de utilidades en Python** que incluye varias funciones, tests automatizados y cobertura de código. Está organizado con buenas prácticas de desarrollo y control de versiones con Git.

---

## 📂 Estructura del proyecto

```
kit_utiles/
│
├── src/                # Código fuente
│   ├── __init__.py
│   └── (módulos .py)
│
├── tests/              # Pruebas unitarias
│   ├── __init__.py
│   └── test_*.py
│
├── pyproject.toml      # Configuración de pytest y cobertura
├── requirements.txt    # Dependencias del proyecto
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.11+
- [pytest](https://docs.pytest.org/en/stable/)
- [pytest-cov](https://pytest-cov.readthedocs.io/)

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🧪 Ejecutar tests y generar cobertura

Desde la raíz del proyecto:

```bash
# Ejecutar tests
pytest -v

# Ejecutar tests con cobertura y generar coverage.xml
pytest --cov=src --cov-report=term --cov-report=xml
```

- `coverage.xml` se genera en la raíz del proyecto.
- Cobertura mínima configurada en `pyproject.toml`: 85%.

---

## 🌿 Control de versiones

- **Rama principal**: `main`
- **Rama de desarrollo**: `develop`
- **Tags**: `v1.0`, etc.

Ejemplo de comandos Git:

```bash
# Cambiar de rama
git checkout main
git checkout -b develop

# Subir rama y tag a remoto
git push origin develop
git push origin v1.0
```

---

## 📌 Buenas prácticas en GitHub

- Se requiere **pull request para merge en `main`**.
- Se exigen **2-3 aprobaciones** según el grupo.
- Se descartan automáticamente revisiones obsoletas (**Dismiss stale reviews**).
- (Opcional) Se requiere **historia lineal**.

---

## 🚀 Uso

Importa los módulos desde `src` en tu proyecto o scripts:

```python
from src.numbers import grade
from src.utils import word_count

resultado = word_count("Hola, hola, ¿qué tal?")
print(resultado)
print(grade(85))
```

---

## 📄 Licencia

MIT License © 2025
