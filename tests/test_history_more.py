import pandas as pd
from app.history import History

class FakeCalc:
    def __init__(self, a, op, b, result):
        self.a, self.op, self.b, self.result = a, op, b, result

def test_history_append_and_replace(tmp_path):
    p = tmp_path / "h.csv"
    h = History(str(p)); h.load()
    h.append(FakeCalc(2, "+", 3, 5))
    h.append(FakeCalc(9, "root", 2, 3))
    assert p.exists()
    assert len(h.to_list()) == 2
    trimmed = h.df.head(1)
    h.replace_with(trimmed)
    assert len(h.to_list()) == 1