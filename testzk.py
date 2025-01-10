from unittest.mock import patch, MagicMock, mock_open
import pytest

# Testy pro Rectangle a Circle
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20  # Plocha obdélníku: 4 * 5 = 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3  # Plocha kruhu: π * 3^2 ≈ 28.3