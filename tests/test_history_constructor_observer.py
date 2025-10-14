from app.history import History

class CaptureObserver:
    def __init__(self): self.rows = []
    def on_append(self, row: dict) -> None:
        self.rows.append(row)

class FakeCalc:
    def __init__(self, a, op, b, result):
        self.a, self.op, self.b, self.result = a, op, b, result

def test_history_constructor_and_observer_loop(tmp_path):
    p = tmp_path / "h.csv"
    cap = CaptureObserver()
    h = History(str(p), observers=[cap])  # covers ctor line ~15
    h.load()
    h.append(FakeCalc(5, "+", 7, 12))     # hits observer loop lines ~5051
    assert len(cap.rows) == 1
