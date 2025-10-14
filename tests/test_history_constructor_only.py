from app.history import History

def test_history_constructor_only(tmp_path):
    h = History(str(tmp_path / "just_ctor.csv"))
    # Ensure default columns exist  this executes the ctor body
    assert set(h.df.columns) == {"timestamp","a","op","b","result"}
