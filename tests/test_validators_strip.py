from app.input_validators import parse_op

def test_parse_op_strips_whitespace():
    assert parse_op("   +   ") == "+"
