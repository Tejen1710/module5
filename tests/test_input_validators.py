import pytest
from app.input_validators import parse_float, parse_op
from app.exceptions import ValidationError

def test_parse_float_ok():
    assert parse_float("3.14") == 3.14

@pytest.mark.parametrize("val", ["x", None, object()])
def test_parse_float_bad(val):
    with pytest.raises(ValidationError):
        parse_float(val)  # type: ignore[arg-type]

@pytest.mark.parametrize("op", ["+","-","*","/","^","root"])
def test_parse_op_ok(op):
    assert parse_op(op) == op

def test_parse_op_bad():
    with pytest.raises(ValidationError):
        parse_op("pow")