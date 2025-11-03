import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from service import add_income, add_expense


def test_add_income():
    assert add_income(100, 50) == 150


def test_add_expense():
    assert add_expense(100, 30) == 70
