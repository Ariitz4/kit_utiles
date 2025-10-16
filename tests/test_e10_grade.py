import pytest
from src.numbers import grade

# Valores límite y calificaciones esperadas
@pytest.mark.parametrize("score, expected", [
    (100, "A"), (90, "A"),
    (89, "B"), (80, "B"),
    (79, "C"), (70, "C"),
    (69, "D"), (60, "D"),
    (59, "F"), (0, "F")
])
def test_grade_boundaries(score, expected):
    assert grade(score) == expected

# Valores fuera de rango
@pytest.mark.parametrize("score", [-1, 101])
def test_grade_out_of_range(score):
    with pytest.raises(ValueError, match="score out of range"):
        grade(score)

# Score no entero
def test_grade_non_integer():
    with pytest.raises(TypeError, match="score must be int"):
        grade(85.0)
