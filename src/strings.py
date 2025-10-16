"""
Módulo strings.py
Funciones de texto para practicar el uso de pytest con fixtures y parametrización.
"""

import re
import unicodedata
from collections import Counter

# -------------------------------------------------------
# Expresiones regulares
# -------------------------------------------------------
_WORD_REGEX = re.compile(r"[a-z]+")  # solo letras minúsculas
_EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,10}$")

# -------------------------------------------------------
# Funciones de utilidad
# -------------------------------------------------------
def _strip_accents(text: str) -> str:
    """
    Quita acentos de un texto (NFD + eliminar marcas de acento).
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )

# -------------------------------------------------------
# Funciones principales
# -------------------------------------------------------
def word_count(text: str) -> dict[str, int]:
    """
    Cuenta la frecuencia de palabras en un texto.
    Normaliza a minúsculas, quita acentos y signos de puntuación.
    """
    text = text.lower()
    text = _strip_accents(text)
    tokens = _WORD_REGEX.findall(text)
    return dict(Counter(tokens))


def validate_email(email: str) -> bool:
    """
    Valida un correo electrónico simple:
      usuario@dominio.tld donde:
        - usuario: letras, números, ., _, -
        - dominio: letras, números, -
        - tld: 2 a 10 letras
    """
    return bool(_EMAIL_REGEX.match(email))

# -------------------------------------------------------
# Ejemplo de uso de word_count
# -------------------------------------------------------
if __name__ == "__main__":
    texto = "¿Qué, qué? ¡Árbol! árbol... ÁrBoL"
    print(word_count(texto))
    print(validate_email("usuario@dominio.com"))
    print(validate_email("correo-invalido@@dominio"))
