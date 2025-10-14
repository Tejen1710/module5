from app.exceptions import CalculatorError, InvalidOperationError

def test_exception_hierarchy():
    assert issubclass(InvalidOperationError, CalculatorError)