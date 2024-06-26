import pytest
from my_funcs import add, subtract, multiply, divide

"""
Run tests
python -m pytest
or
python -m pytest test_calculator.py
"""

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)
