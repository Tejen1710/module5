import pytest
from app.operations import make_operation
from app.exceptions import InvalidOperationError

def test_root_zero_invalid():
    with pytest.raises(InvalidOperationError):
        make_operation("root").execute(9, 0)
