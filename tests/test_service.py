import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from service import add_income, add_expense
def test_add_income():
    assert add_income(100, 50) == 150

def test_add_expense():
    assert add_expense(200, 50) == 150
