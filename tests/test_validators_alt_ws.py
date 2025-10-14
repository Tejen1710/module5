from app.input_validators import parse_op

def test_parse_op_alt_whitespace_variant():
    assert parse_op("\t+\n") == "+"
