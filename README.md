
# Enhanced Calculator (Module 5)
![CI Status](https://github.com/Tejen1710/module5/actions/workflows/python-app.yml/badge.svg)

A modular CLI calculator using **Strategy**, **Factory**, **Observer**, **Memento**, and a **Calculator Facade**.  
History is stored in **pandas** and auto-saved to **CSV**.  
Fully tested with `pytest` and enforced **100% coverage** via CI.

---

## 🚀 Quickstart

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m app.calculator_repl
```
## 🕹️ Commands
calc <a> <op> <b> → operations: + - * / ^ root

history → show persisted history

clear → wipe history

undo / redo

save / load

help, exit

## 🧪 Testing
```
pytest
```
Coverage threshold is configured at 100% in pytest.ini.

## 🧰 Design Patterns
Strategy – operation classes (Add, Subtract, Multiply, Divide, Power, Root)

Factory – make_operation() builds strategies dynamically by symbol

Observer – LoggerObserver, AutoSaveObserver for logging and autosave

Memento – Caretaker + HistoryMemento enable undo/redo

Facade – Calculator exposes compute, undo, redo over subsystems

## ⚙️ Configuration
Environment variables via .env:

Variable	Default	Description
APP_HISTORY_PATH	history.csv	CSV path for persisted history
APP_AUTO_SAVE	true	Auto-save after each operation
APP_LOG_OBSERVER	true	Enable logging observer

Example .env
```
APP_HISTORY_PATH=history.csv
APP_AUTO_SAVE=true
APP_LOG_OBSERVER=true
```
## 📝 Notes to Reach / Keep 100% Coverage
Use parameterized tests for operations and validators (✅ done).

Add REPL tests for calc and error paths (invalid op, NaN inputs).

Exclude harmless no-ops (like unreachable branches) using # pragma: no cover.

## 🧭 Git & GitHub Setup (Brief)
bash
Copy code
echo "# Enhanced Calculator" > README.md
git init -b main
git add .
git commit -m "feat: initial scaffold for Module 5"
git remote add origin https://github.com/your_github_username/enhanced-calculator.git
<<<<<<< HEAD
git push -u origin main
## 📄 License
MIT License
=======
git push -u origin main
>>>>>>> b52bfd8 (chore: save local changes)
