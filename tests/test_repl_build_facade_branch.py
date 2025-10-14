from app.calculator_repl import build_facade
from app.calculator_config import AppConfig

def test_build_facade_log_observer(tmp_path):
    cfg = AppConfig(
        history_path=str(tmp_path / "h.csv"),
        auto_save=True,
        log_observer=True,   # forces the branch that appends LoggerObserver
    )
    calc = build_facade(cfg)
    # Verify a LoggerObserver is present
    names = [obs.__class__.__name__ for obs in calc._history._observers]
    assert "LoggerObserver" in names
