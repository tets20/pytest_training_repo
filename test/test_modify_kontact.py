# -*- coding: utf-8 -*-

from model.kontact import Kontact

def test_modify_kontact_firstname(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test"))
    old_kontacts = app.kontact.get_kontact_list()
    kontact = Kontact(firstname="Test_contact!!!")
    kontact.id = old_kontacts[0].id
    app.kontact.modify_first_kontact(kontact)
    new_kontacts = app.kontact.get_kontact_list()
    assert len(old_kontacts) == len(new_kontacts)
    old_kontacts[0] = kontact
    assert sorted(old_kontacts, key=Kontact.id_or_max) == sorted(new_kontacts, key=Kontact.id_or_max)


def test_modify_kontact_middlename(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test"))
    old_kontacts = app.kontact.get_kontact_list()
    kontact = Kontact(middlename="Test_contact!!!")
    kontact.id = old_kontacts[0].id
    app.kontact.modify_first_kontact(kontact)
    new_kontacts = app.kontact.get_kontact_list()
    assert len(old_kontacts) == len(new_kontacts)
    old_kontacts[0] = kontact
    assert sorted(old_kontacts, key=Kontact.id_or_max) == sorted(new_kontacts, key=Kontact.id_or_max)