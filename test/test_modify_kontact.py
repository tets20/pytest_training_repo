# -*- coding: utf-8 -*-

from model.kontact import Kontact
from random import randrange

def test_modify_kontact_firstname(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test"))
    old_kontacts = app.kontact.get_kontact_list()
    index = randrange(len(old_kontacts))
    kontact = Kontact(firstname="Test_contact!!!")
    kontact.id = old_kontacts[index].id
    app.kontact.modify_kontact_by_index(kontact,index)
    assert len(old_kontacts) == app.kontact.count()
    new_kontacts = app.kontact.get_kontact_list()
    old_kontacts[index] = kontact
    assert sorted(old_kontacts, key=Kontact.id_or_max) == sorted(new_kontacts, key=Kontact.id_or_max)


def test_modify_kontact_middlename(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test"))
    old_kontacts = app.kontact.get_kontact_list()
    index = randrange(len(old_kontacts))
    kontact = Kontact(middlename="Test_contact!!!")
    kontact.id = old_kontacts[index].id
    app.kontact.modify_kontact_by_index(kontact,index)
    assert len(old_kontacts) == app.kontact.count()
    new_kontacts = app.kontact.get_kontact_list()
    old_kontacts[index] = kontact
    assert sorted(old_kontacts, key=Kontact.id_or_max) == sorted(new_kontacts, key=Kontact.id_or_max)