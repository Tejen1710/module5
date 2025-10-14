import pandas as pd
from app.history import History

class FakeCalc:
    def __init__(self, a, op, b, result):
        self.a, self.op, self.b, self.result = a, op, b, result

def test_history_adds_missing_columns(tmp_path):
    p = tmp_path / "lbly.csv"
    h = History(str(p))
    h.load()
    # Create a frame intentionally missing the "result" column
    h.df = pd.DataFrame(columns=["timestamp","a","op","b"])
    # Append triggers the "missing columns" branch (lines ~5051)
    h.append(FakeCalc(3, "+", 4, 7))
    assert "result" in h.df.columns
