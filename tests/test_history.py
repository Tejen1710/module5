from app.history import History

def test_history_load_save(tmp_path):
    p = tmp_path/"h.csv"
    h = History(str(p))
    h.load()  # file not found => empty DataFrame
    assert h.df.empty
    h.save()  # creates file
    h.clear()
    assert h.df.empty