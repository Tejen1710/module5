from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, Callable
from .exceptions import DivisionByZeroError, InvalidOperationError

# Strategy protocol
class Operation(Protocol):
    def execute(self, a: float, b: float) -> float: ...

@dataclass
class Add:
    def execute(self, a: float, b: float) -> float:
        return a + b

@dataclass
class Subtract:
    def execute(self, a: float, b: float) -> float:
        return a - b

@dataclass
class Multiply:
    def execute(self, a: float, b: float) -> float:
        return a * b

@dataclass
class Divide:
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return a / b

@dataclass
class Power:
    def execute(self, a: float, b: float) -> float:
        return a ** b

@dataclass
class Root:
    def execute(self, a: float, b: float) -> float:
        # interpret as b-th root of a
        if b == 0:
            raise InvalidOperationError("0-th root is undefined")
        # negative with fractional root would error in real domain; let Python raise
        return a ** (1.0 / b)

# Factory pattern
_FACTORY: dict[str, Callable[[], Operation]] = {
    "+": Add,
    "-": Subtract,
    "*": Multiply,
    "/": Divide,
    "^": Power,
    "root": Root,
}

def make_operation(op_symbol: str) -> Operation:
    key = op_symbol.strip().lower()
    if key not in _FACTORY:
        raise InvalidOperationError(f"Unknown operation: {op_symbol}")
    return _FACTORY[key]()