# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    radius = 1
    result = area_of_circle(radius)
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    radius = 0
    result = area_of_circle(radius)
    assert result == 0


def test_area_of_circle_negative_radius():
    with pytest.raises(ValueError):
        area_of_circle(-5)


def test_get_nth_fibonacci_zero():
    result = get_nth_fibonacci(0)
    assert result == 0


def test_get_nth_fibonacci_one():
    result = get_nth_fibonacci(1)
    assert result == 1


def test_get_nth_fibonacci_ten():
    result = get_nth_fibonacci(10)
    assert result == 55


def test_get_nth_fibonacci_large():
    assert get_nth_fibonacci(6) == 8
