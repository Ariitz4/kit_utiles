from src.numbers import sum_list
import pytest

def test_sum_list_with_numbers():
    # Arrange
    numbers = [1, 2, 3, 4]

    # Act
    result = sum_list(numbers)

    # Assert
    assert result == 10


def test_sum_list_with_empty_list():
    # Arrange
    numbers = []

    # Act
    result = sum_list(numbers)

    # Assert
    assert result == 0