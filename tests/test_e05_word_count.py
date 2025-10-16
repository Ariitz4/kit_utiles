import pytest
from src.strings import word_count

@pytest.fixture
def texto():
    return "Hola, hola... ¿Que tal? Tal vez bien: hola!"

def test_word_count(texto):
    resultado = word_count(texto)
    assert resultado.get("hola") == 3
    assert resultado.get("tal") == 2
    assert resultado.get("que") == 1
    assert "inexistente" not in resultado