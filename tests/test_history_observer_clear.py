from app.history import History

class SpyObserver:
    def __init__(self):
        self.seen = []
    def on_append(self, row: dict) -> None:
        self.seen.append(row)

class FakeCalc:
    def __init__(self, a, op, b, result):
        self.a, self.op, self.b, self.result = a, op, b, result

def test_history_observer_and_clear(tmp_path):
    p = tmp_path / "h.csv"
    spy = SpyObserver()
    h = History(str(p), observers=[spy])   # covers constructor/columns (~15)
    h.load()
    h.append(FakeCalc(2, "+", 3, 5))       # fires observer (~5051)
    assert len(spy.seen) == 1
    assert p.exists()                      # append autosave (~54)
    h.clear()                              # clear triggers save as well
    assert p.exists()
    assert len(h.to_list()) == 0
