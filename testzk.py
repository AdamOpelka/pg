from unittest.mock import patch, MagicMock, mock_open
from zkouska_cv3 import Rectangle, Circle
import pytest


rect = Rectangle(4, 5)
print(f"Rectangle (4x5) area: {rect.area()}")  # Očekávaný výsledek: 20

circle = Circle(3)
print(f"Circle (radius 3) area: {circle.area():.2f}")  # Očekávaný výsledek: přibližně 28.27

# Další testy
rect2 = Rectangle(10, 10)
print(f"Rectangle (10x10) area: {rect2.area()}")  # Očekávaný výsledek: 100

circle2 = Circle(1)
print(f"Circle (radius 1) area: {circle2.area():.2f}")  # Očekávaný výsledek: přibližně 3.14