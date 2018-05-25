from model.kontact import Kontact
import random

def test_delete_some_kontact(app,db,check_ui):
    if len(db.get_kontact_list()) == 0:
        app.kontact.create(Kontact(firstname="test"))
    old_kontacts = db.get_kontact_list()
    kontact = random.choice(old_kontacts)
    app.kontact.delete_kontact_by_id(kontact.id)
    assert len(old_kontacts) - 1 == app.kontact.count()
    new_kontacts = db.get_kontact_list()
    old_kontacts.remove(kontact) #написать метод
    assert old_kontacts == new_kontacts
    if check_ui:
        assert sorted(new_kontacts, key=Kontact.id_or_max) == sorted(app.kontact.get_kontact_list(),key=Kontact.id_or_max)
