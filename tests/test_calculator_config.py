import pytest
from app.calculator_config import AppConfig, ConfigError

def test_from_env_defaults(monkeypatch):
    for k in ("APP_HISTORY_PATH","APP_AUTO_SAVE","APP_LOG_OBSERVER"):
        monkeypatch.delenv(k, raising=False)
    cfg = AppConfig.from_env()
    assert cfg.history_path.endswith("history.csv")
    assert cfg.auto_save is True
    assert cfg.log_observer is True

def test_empty_path(monkeypatch):
    monkeypatch.setenv("APP_HISTORY_PATH", " ")
    with pytest.raises(ConfigError):
        AppConfig.from_env()