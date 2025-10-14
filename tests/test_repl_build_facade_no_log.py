from app.calculator_repl import build_facade
from app.calculator_config import AppConfig

def test_build_facade_no_log_observer(tmp_path):
    cfg = AppConfig(
        history_path=str(tmp_path / "h.csv"),
        auto_save=True,
        log_observer=False,  # hit the FALSE branch of line 41
    )
    calc = build_facade(cfg)
    # ensure no LoggerObserver attached
    names = [obs.__class__.__name__ for obs in calc._history._observers]
    assert "LoggerObserver" not in names
