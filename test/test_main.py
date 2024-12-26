import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import factorial


def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(6) == 720

def test_factorial_large_number():
    assert factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError, match="Факториал не определен для отрицательных чисел."):
        factorial(-1)
