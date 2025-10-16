import pytest
from src.strings import validate_email

# Emails válidos
@pytest.mark.parametrize("email", [
    "user@example.com",
    "nombre.apellido@dominio-es.org",
    "u_1-2@dominio.net"
])
def test_valid_emails(email):
    assert validate_email(email) is True

# Emails inválidos
@pytest.mark.parametrize("email", [
    "sin_arroba.com",
    "user@dominio.",
    "user@dominio.c",
    "user@.com",
    "@dominio.com",
    "user@dominio..com"
])
def test_invalid_emails(email):
    assert validate_email(email) is False