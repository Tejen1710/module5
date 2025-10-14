from app.calculator_repl import build_facade
from app.calculator_config import AppConfig

def test_build_facade_attaches_logger_observer(tmp_path):
    cfg = AppConfig(
        history_path=str(tmp_path / "hist.csv"),
        auto_save=True,
        log_observer=True,  # hit TRUE branch (~41)
    )
    calc = build_facade(cfg)
    names = [obs.__class__.__name__ for obs in calc._history._observers]
    assert "LoggerObserver" in names
