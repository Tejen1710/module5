from app.calculation import Calculator
from app.calculator_memento import Caretaker
from app.history import History

class DummyCaretaker(Caretaker):
    def snapshot(self, history):
        super().snapshot(history)

def test_calculation_and_history(tmp_path):
    hist = History(tmp_path/"h.csv")
    hist.load()
    care = DummyCaretaker()
    calc = Calculator(hist, care)
    c = calc.compute(2, "+", 3)
    assert c.result == 5
    assert len(hist.to_list()) == 1