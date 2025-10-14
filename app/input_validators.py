from __future__ import annotations
from .exceptions import ValidationError

def parse_float(s: str) -> float:
    try:
        return float(s)
    except (TypeError, ValueError) as e:
        raise ValidationError(f"Not a number: {s}") from e

_ALLOWED = {"+","-","*","/","^","root"}

def parse_op(s: str) -> str:
    if s is None:
        raise ValidationError("Operation missing")
    t = s.strip().lower()
    if t not in _ALLOWED:
        raise ValidationError(f"Unsupported operation: {s}")
    return t