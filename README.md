# Enhanced Calculator (Module 5)

A modular CLI calculator using Strategy, Factory, Observer, Memento, and a Calculator Facade. History stored in pandas and auto-saved to CSV. Fully tested with `pytest` and enforced 100% coverage via CI.

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m app.calculator_repl
Commands
• calc <a> <op> <b> ops: + - * / ^ root
• history show persisted history
• clear wipe history
• undo / redo
• save / load
• help, exit
Testing
pytest
Coverage threshold is configured at 100% in pytest.ini.
Design Patterns
• Strategy: operation classes (Add, Subtract, …)
• Factory: make_operation() builds strategies by symbol
• Observer: LoggerObserver, AutoSaveObserver concept
• Memento: Caretaker + HistoryMemento for undo/redo
• Facade: Calculator exposes compute/undo/redo over subsystems
Configuration
Environment variables via .env: - APP_HISTORY_PATH (default history.csv) - APP_AUTO_SAVE (default true) - APP_LOG_OBSERVER (default true)

---

## 📝 Notes to reach/keep 100% Coverage
- Use parameterized tests for operations and validators (done).
- Add REPL tests for `calc`, error paths (invalid op, NaN inputs).
- Exclude harmless no-ops (like unreachable branches) with `# pragma: no cover` (already shown).

---

## 🧭 Git & GitHub Setup (brief)
```bash
echo "# Enhanced Calculator" > README.md
git init -b main
git add .
git commit -m "feat: initial scaffold for Module 5"
git remote add origin https://github.com/your_github_username/enhanced-calculator.git
git push -u origin main
You’re ready to submit your repo URL to Canvas.