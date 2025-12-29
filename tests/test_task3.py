from src.task3 import add


def test_add_positive() -> None:
    assert add(1, 2) == 3


def test_add_negative() -> None:
    assert add(-1, -1) == -2


def test_add_zero() -> None:
    assert add(0, 5) == 5


def test_add_float() -> None:
    assert add(1.5, 0.5) == 2.0
