from src.numbers import unique_sorted

def test_unique_sorted_numbers():
    assert unique_sorted([3, 1, 2, 3, 2]) == [1, 2, 3]

def test_unique_sorted_strings():
    assert unique_sorted(["b", "a", "b"]) == ["a", "b"]