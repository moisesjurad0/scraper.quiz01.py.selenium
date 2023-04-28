"""sumary_line."""

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


def suma_2enteros(x: int, y: int) -> int:
    """_summary_.

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: _description_
    """
    return x + y


def tsuma_2enteros():
    """_summary_."""
    print("It is", "number" + 1)
    assert suma_2enteros('1', '2') == 10


def greeting(name: str):
    """_summary_.

    Args:
        name (str): _description_

    Returns:
        str: _description_
    """
    return None


# Argument 1 to "greeting" has incompatible type "int"; expected "str"
# greeting(3)
# Argument 1 to "greeting" has incompatible type "bytes"; expected "str"

# uncomment this to force mypy error
# greeting(b'Alice')
# greeting("World!")  # No error
# suma_2enteros('1', '2')
