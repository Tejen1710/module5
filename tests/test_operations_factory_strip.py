from app.operations import make_operation

def test_factory_strips_and_lowercases():
    op = make_operation("  ROOT  ")
    assert abs(op.execute(16, 2) - 4.0) < 1e-9
