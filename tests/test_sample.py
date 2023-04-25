"""sumary_line. """

import pytest


def sumOne(x):
    """_summary_.

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    return x + 1


def test_sumOne():
    """_summary_."""
    assert sumOne(3) == 4


@pytest.mark.parametrize(
    "a,b",
    [
        (1, 2),
        (1, 2),
        (2, 3),
        (3, 4),
        (3, 4)
    ]
)
def test_multi_sumOne(a, b):
    """_summary_.

    Args:
        a (_type_): _description_
        b (_type_): _description_
    """
    assert sumOne(a) == b


def sumTwo(x):
    """_summary_.

    Args:
        x (_type_): _description_

    Returns:
        _type_: _description_
    """
    return x + 2


@pytest.mark.parametrize(
    "a,b",
    [
        (1, 3),
        (1, 3),
        (2, 4),
        (3, 5),
        (3, 5)
    ]
)
def test_multi_sumTwo(a, b):
    """_summary_.

    Args:
        a (_type_): _description_
        b (_type_): _description_
    """
    assert sumTwo(a) == b
