from model.kontact import Kontact
from random import randrange

def test_delete_some_kontact(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test"))
    old_groups = app.kontact.get_kontact_list()
    index = randrange(len(old_groups))
    app.kontact.delete_kontact_by_index(index)
    assert len(old_groups) - 1 == app.kontact.count()
    new_groups = app.kontact.get_kontact_list()
    old_groups[index:index + 1] = []
    assert old_groups == new_groups

