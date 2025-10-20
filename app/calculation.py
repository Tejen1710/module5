from __future__ import annotations
from dataclasses import dataclass
from .operations import Operation, make_operation

@dataclass(frozen=True)
class Calculation:
    a: float
    op: str
    b: float
    result: float

class Calculator:
    """Facade: simple interface over operations & history/memento (injected)."""
    def __init__(self, history, caretaker):
        self._history = history
        self._caretaker = caretaker

    def compute(self, a: float, op_symbol: str, b: float) -> Calculation:
        op: Operation = make_operation(op_symbol)
        result = op.execute(a, b)
        calc = Calculation(a=a, op=op_symbol, b=b, result=result)
        self._history.append(calc)
        self._caretaker.snapshot(self._history)
        return calc

    # convenience wrappers
    def undo(self) -> None:
        self._caretaker.undo(self._history)

    def redo(self) -> None:
        self._caretaker.redo(self._history)