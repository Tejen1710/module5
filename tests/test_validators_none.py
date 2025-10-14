import pytest
from app.input_validators import parse_op
from app.exceptions import ValidationError

def test_parse_op_none_raises():
    with pytest.raises(ValidationError):
        parse_op(None)  # type: ignore[arg-type]
