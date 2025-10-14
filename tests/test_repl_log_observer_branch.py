import builtins
from app.calculator_repl import run

def test_repl_log_observer_branch(monkeypatch, tmp_path):
    monkeypatch.setenv("APP_HISTORY_PATH", str(tmp_path / "hist.csv"))
    monkeypatch.setenv("APP_LOG_OBSERVER", "true")   # <- forces LoggerObserver path
    monkeypatch.setenv("APP_AUTO_SAVE", "true")
    seq = ["exit"]  # build facade then exit immediately
    monkeypatch.setattr(builtins, "input", lambda prompt="": seq.pop(0))
    assert run() == 0
