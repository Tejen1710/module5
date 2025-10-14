from app.history import History

def test_history_ctor_default_observers(tmp_path):
    h = History(str(tmp_path / "ctor_default.csv"))  # use default observers=()
    # basic sanity checks so the ctor work is exercised
    assert list(h.df.columns) == ["timestamp","a","op","b","result"]
    assert h._loaded is False
    assert isinstance(h._observers, list)
    assert h._observers == []
