# -*- coding: utf-8 -*-

from model.kontact import Kontact



def test_add_kontact(app,json_kontacts):
    kontact = json_kontacts
    old_kontacts = app.kontact.get_kontact_list()
    app.kontact.create(kontact)
    assert len(old_kontacts) + 1 == app.kontact.count()
    new_kontacts = app.kontact.get_kontact_list()
    old_kontacts.append(kontact)
    assert sorted(old_kontacts, key = Kontact.id_or_max) == sorted(new_kontacts, key = Kontact.id_or_max)




