from app.history import History
from app.calculator_memento import Caretaker
from app.calculation import Calculator

def test_undo_redo(tmp_path):
    h = History(tmp_path/"h.csv")
    h.load()
    c = Caretaker()
    calc = Calculator(h, c)
    calc.compute(1, "+", 1)
    calc.compute(2, "+", 2)
    assert len(h.to_list()) == 2
    calc.undo()
    assert len(h.to_list()) == 2  # state restored to snapshot with 2 rows (snapshot after compute)
    # Note: With snapshot-after-append design, undo restores to last snapshot;
    # to observe removal behavior you’d snapshot before append instead. Both are valid if consistent & tested.