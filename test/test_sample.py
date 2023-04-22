# content of test_sample.py
import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


@pytest.mark.parametrize(
    "a,b",
    [
        (1, 1),
        (1, 2),
        (2, 2),
        (3, 3),
        (3, 4)
    ]
)
def test_multi_sum(a, b):
    assert func(a) == b
