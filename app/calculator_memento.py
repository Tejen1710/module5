from __future__ import annotations

class HistoryMemento:
    def __init__(self, df):
        # deep copy to freeze state
        self._state = df.copy(deep=True)

    def restore(self, history) -> None:
        history.replace_with(self._state)

class Caretaker:
    def __init__(self):
        self._undos: list[HistoryMemento] = []
        self._redos: list[HistoryMemento] = []

    def snapshot(self, history) -> None:
        self._undos.append(HistoryMemento(history.df))
        self._redos.clear()

    def undo(self, history) -> None:
        if not self._undos:
            return  # pragma: no cover (no-op)
        m = self._undos.pop()
        self._redos.append(HistoryMemento(history.df))
        m.restore(history)

    def redo(self, history) -> None:
        if not self._redos:
            return  # pragma: no cover (no-op)
        m = self._redos.pop()
        self._undos.append(HistoryMemento(history.df))
        m.restore(history)