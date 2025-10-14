from app.history import History, LoggerObserver

class SpyObserver:
    def __init__(self): self.rows = []
    def on_append(self, row: dict) -> None:
        self.rows.append(row)

class FakeCalc:
    def __init__(self, a, op, b, result):
        self.a, self.op, self.b, self.result = a, op, b, result

def test_history_two_observers_loop(tmp_path):
    p = tmp_path / "hist.csv"
    spy = SpyObserver()
    h = History(str(p), observers=[LoggerObserver(), spy])  # ctor (+ at least 2 observers)
    h.load()
    h.append(FakeCalc(1, "+", 2, 3))  # triggers observer loop (lines ~5051)
    assert len(spy.rows) == 1
