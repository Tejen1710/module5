import pytest
from app.operations import make_operation
from app.exceptions import DivisionByZeroError, InvalidOperationError

@pytest.mark.parametrize("op,a,b,expected", [
    ("+", 1, 2, 3),
    ("-", 5, 2, 3),
    ("*", 3, 4, 12),
    ("/", 12, 3, 4),
    ("^", 2, 3, 8),
    ("root", 9, 2, 3),
])
def test_ops(op, a, b, expected):
    assert make_operation(op).execute(a, b) == pytest.approx(expected)

def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        make_operation("/").execute(1, 0)

def test_unknown_op():
    with pytest.raises(InvalidOperationError):
        make_operation("?")