from app.operations import make_operation

def test_factory_strip_lower_alt_symbol():
    # Mixed case, trailing/leading spaces  should still resolve
    op = make_operation("  ^  ")
    assert op.execute(2, 4) == 16
