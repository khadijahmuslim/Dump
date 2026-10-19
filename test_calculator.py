import pytest

from calculator import add, substract, multiply, divide

def test_add():
  assert add(2, 3) == 5

def test_subsract():
  assert substract(5, 3) == 2

def test_multiply():
  assert multiply(4, 3) == 12

def test_divide():
  assert divide(10, 2) == 5

def test_divide_by_zero():
  with pytest.raise(ValueError):
    divide(10,0)
