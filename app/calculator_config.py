from __future__ import annotations
import os
from dataclasses import dataclass
from dotenv import load_dotenv

class ConfigError(Exception):
    pass

@dataclass(frozen=True)
class AppConfig:
    history_path: str
    auto_save: bool
    log_observer: bool

    @staticmethod
    def from_env() -> "AppConfig":
        load_dotenv()
        path = os.getenv("APP_HISTORY_PATH", "history.csv")
        auto = os.getenv("APP_AUTO_SAVE", "true").lower() in {"1", "true", "yes", "y"}
        log_obs = os.getenv("APP_LOG_OBSERVER", "true").lower() in {"1", "true", "yes", "y"}
        if not path.strip():
            raise ConfigError("APP_HISTORY_PATH cannot be empty")
        return AppConfig(history_path=path, auto_save=auto, log_observer=log_obs)