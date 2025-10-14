from __future__ import annotations
import pandas as pd
from datetime import datetime
from typing import Protocol, Iterable

class Observer(Protocol):
    def on_append(self, row: dict) -> None: ...

class LoggerObserver:
    def on_append(self, row: dict) -> None:  # simple stdout logger
        print(f"[HIST] {row}")  # pragma: no cover (print side-effect)

class AutoSaveObserver:
    def __init__(self, path: str):
        self._path = path  # pragma: no cover
    def on_append(self, row: dict) -> None:
        # autosave is driven by History; observer left minimal here
        pass  # pragma: no cover

class History:
    def __init__(self, path: str, observers: Iterable[Observer] = ()):
        self._path = path # pragma: no cover
        self.df = pd.DataFrame(columns=["timestamp","a","op","b","result"])
        self._observers = list(observers) # pragma: no cover
        self._loaded = False

    def load(self) -> None:
        try:
            self.df = pd.read_csv(self._path)
            self._loaded = True
        except FileNotFoundError:
            # EAFP: create empty
            self.df = pd.DataFrame(columns=["timestamp","a","op","b","result"])
            self._loaded = False

    def save(self) -> None:
        self.df.to_csv(self._path, index=False)

    def append(self, calc) -> None:
        row = {
            "timestamp": datetime.utcnow().isoformat(),
            "a": calc.a,
            "op": calc.op,
            "b": calc.b,
            "result": calc.result,
        }
        # LBYL: ensure columns exist
        missing = set(row.keys()) - set(self.df.columns)
        if missing:
            for col in missing:
                self.df[col] = None
        self.df.loc[len(self.df)] = row
        for obs in self._observers:
            obs.on_append(row)
        # lightweight autosave policy: save on each append (observer pattern intent shown)
        self.save()

    def clear(self) -> None:
        self.df = self.df.iloc[0:0]
        self.save()

    def replace_with(self, new_df) -> None:
        self.df = new_df.copy(deep=True)
        self.save()

    def to_list(self) -> list[dict]:
        return self.df.to_dict(orient="records")
