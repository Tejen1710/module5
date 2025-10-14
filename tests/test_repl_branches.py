import builtins
from app.calculator_repl import run

class FakeIn:
    def __init__(self, lines):
        self._it = iter(lines)
    def __call__(self, prompt=""):
        return next(self._it)

def test_repl_with_logger_and_usage(monkeypatch, tmp_path):
    # Turn ON LoggerObserver to hit the branch (lines ~24/41)
    monkeypatch.setenv("APP_HISTORY_PATH", str(tmp_path / "hist.csv"))
    monkeypatch.setenv("APP_LOG_OBSERVER", "true")
    monkeypatch.setenv("APP_AUTO_SAVE", "true")
    seq = [
        "help",
        "calc 2 +",       # wrong arity -> prints usage (hits ~7071)
        "unknowncmd",     # unknown command branch
        "exit",
    ]
    monkeypatch.setattr(builtins, "input", FakeIn(seq))
    assert run() == 0

def test_repl_keyboardinterrupt(monkeypatch, tmp_path):
    monkeypatch.setenv("APP_HISTORY_PATH", str(tmp_path / "hist.csv"))
    monkeypatch.setenv("APP_LOG_OBSERVER", "false")
    monkeypatch.setenv("APP_AUTO_SAVE", "true")
    def boom(prompt=""):
        raise KeyboardInterrupt
    monkeypatch.setattr(builtins, "input", boom)
    assert run() == 0

def test_repl_eoferror(monkeypatch, tmp_path):
    monkeypatch.setenv("APP_HISTORY_PATH", str(tmp_path / "hist.csv"))
    monkeypatch.setenv("APP_LOG_OBSERVER", "false")
    monkeypatch.setenv("APP_AUTO_SAVE", "true")
    def eof(prompt=""):
        raise EOFError
    monkeypatch.setattr(builtins, "input", eof)
    assert run() == 0
