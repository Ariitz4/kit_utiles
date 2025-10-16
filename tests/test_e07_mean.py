import pytest
from src.numbers import mean

def test_mean_numbers():
    assert mean([1, 2, 3, 4]) == 2.5

def test_mean_empty_list():
    with pytest.raises(ValueError, match="empty sequence"):
        mean([])