import builtins
from app.calculator_repl import run

class FakeIn:
    def __init__(self, lines):
        self._lines = iter(lines)
    def __call__(self, prompt=""):
        return next(self._lines)

def test_repl_help_exit(monkeypatch):
    seq = ["help", "exit"]
    monkeypatch.setenv("APP_HISTORY_PATH", "test_hist.csv")
    monkeypatch.setenv("APP_LOG_OBSERVER", "false")
    monkeypatch.setenv("APP_AUTO_SAVE", "false")
    monkeypatch.setattr(builtins, "input", FakeIn(seq))
    rc = run()
    assert rc == 0