# -*- coding: utf-8 -*-

from model.kontact import Kontact
import random

def test_modify_kontact_firstname(app,db,check_ui):
    if len(db.get_kontact_list()) == 0:
        app.kontact.create(Kontact(firstname="test"))
    old_kontacts = db.get_kontact_list()
    kontact = random.choice(old_kontacts)
    kontact_mod = Kontact(firstname="Test_contact!!!")
    app.kontact.modify_kontact_by_id(kontact.id,kontact_mod)
    assert len(old_kontacts) == app.kontact.count()
    new_kontacts = db.get_kontact_list()
    assert sorted(old_kontacts, key=Kontact.id_or_max) == sorted(new_kontacts, key=Kontact.id_or_max)
    if check_ui:
        assert sorted(new_kontacts, key=Kontact.id_or_max) == sorted(app.kontact.get_kontact_list(),key=Kontact.id_or_max)


def test_modify_kontact_middlename(app,db,check_ui):
    if len(db.get_kontact_list()) == 0:
        app.kontact.create(Kontact(firstname="test"))
    old_kontacts = db.get_kontact_list()
    kontact = random.choice(old_kontacts)
    kontact_mod = Kontact(middlename="Test_contact!!!")
    app.kontact.modify_kontact_by_id(kontact.id, kontact_mod)
    assert len(old_kontacts) == app.kontact.count()
    new_kontacts = db.get_kontact_list()
    assert sorted(old_kontacts, key=Kontact.id_or_max) == sorted(new_kontacts, key=Kontact.id_or_max)
    if check_ui:
        assert sorted(new_kontacts, key=Kontact.id_or_max) == sorted(app.kontact.get_kontact_list(),key=Kontact.id_or_max)