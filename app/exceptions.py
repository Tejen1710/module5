class CalculatorError(Exception):
    """Base error for calculator domain."""

class InvalidOperationError(CalculatorError):
    pass

class DivisionByZeroError(CalculatorError):
    pass

class ValidationError(CalculatorError):
    pass