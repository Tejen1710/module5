import builtins, os
from app.calculator_repl import run

class FakeIn:
    def __init__(self, lines): self._it = iter(lines)
    def __call__(self, prompt=""): return next(self._it)

def test_repl_full_flow(monkeypatch, tmp_path):
    hist = tmp_path / "hist.csv"
    monkeypatch.setenv("APP_HISTORY_PATH", str(hist))
    monkeypatch.setenv("APP_LOG_OBSERVER", "false")
    monkeypatch.setenv("APP_AUTO_SAVE", "true")
    seq = [
        "help", "foo",
        "calc 2 + 3",
        "calc 9 root 2",
        "calc 1 / 0",
        "calc 2 ? 3",
        "history", "save", "load",
        "undo", "redo",
        "clear",
        "exit",
    ]
    monkeypatch.setattr(builtins, "input", FakeIn(seq))
    rc = run()
    assert rc == 0
    assert hist.exists()