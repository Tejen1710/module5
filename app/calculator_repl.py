from __future__ import annotations
import sys
from .calculator_config import AppConfig
from .calculation import Calculator
from .calculator_memento import Caretaker
from .history import History, LoggerObserver
from .input_validators import parse_float, parse_op
from .exceptions import CalculatorError

HELP = """
Commands:
  calc <a> <op> <b>    Perform calculation. ops: + - * / ^ root
  history              Show history
  clear                Clear history (and save)
  undo | redo          Undo/Redo last history change
  save | load          Save or load history CSV
  help                 Show this help
  exit                 Quit
"""

def build_facade(cfg: AppConfig) -> Calculator:
    observers = []
    if cfg.log_observer:  # pragma: no branch
        observers.append(LoggerObserver()) # pragma: no cover
    history = History(cfg.history_path, observers)
    history.load()
    caretaker = Caretaker()
    # take initial snapshot of loaded state
    caretaker.snapshot(history)
    return Calculator(history, caretaker)


def run() -> int:
    cfg = AppConfig.from_env()
    calc = build_facade(cfg)
    print("Enhanced Calculator. Type 'help' to begin.")
    while True:
        try:
            raw = input(">> ").strip()
            if not raw:
                continue
            parts = raw.split()
            cmd = parts[0].lower()

            if cmd == "exit":
                return 0
            if cmd == "help":
                print(HELP)
                continue
            if cmd == "history":
                for r in calc._history.to_list():
                    print(r)
                continue
            if cmd == "clear":
                calc._history.clear()
                calc._caretaker.snapshot(calc._history)
                print("History cleared.")
                continue
            if cmd == "undo":
                calc.undo(); print("Undone."); continue
            if cmd == "redo":
                calc.redo(); print("Redone."); continue
            if cmd == "save":
                calc._history.save(); print("Saved."); continue
            if cmd == "load":
                calc._history.load(); calc._caretaker.snapshot(calc._history); print("Loaded."); continue

            if cmd == "calc":
                if len(parts) != 4:
                    print("Usage: calc <a> <op> <b>")
                    continue
                a = parse_float(parts[1])
                op = parse_op(parts[2])
                b = parse_float(parts[3])
                c = calc.compute(a, op, b)
                print(f"= {c.result}")
                continue

            print("Unknown command. Type 'help'.")
        except CalculatorError as ce:
            print(f"Error: {ce}")
        except KeyboardInterrupt:
            print("\nBye!")
            return 0
        except EOFError:
            return 0

if __name__ == "__main__":  # pragma: no cover
    sys.exit(run())
