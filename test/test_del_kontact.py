from model.kontact import Kontact

def test_delete_first_kontact(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test"))
    old_groups = app.kontact.get_kontact_list()
    app.kontact.delete_first_kontact()
    new_groups = app.kontact.get_kontact_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups

