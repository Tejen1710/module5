from app.history import History

class DummyObserver:
    def on_append(self, row: dict) -> None:
        pass

def test_history_ctor_with_observers(tmp_path):
    p = tmp_path / "hist.csv"
    h = History(str(p), observers=(DummyObserver(),))  # exercise non-default ctor path (~15)
    assert any(isinstance(o, DummyObserver) for o in h._observers)
