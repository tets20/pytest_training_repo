# -*- coding: utf-8 -*-

from model.kontact import Kontact

def test_modify_contact_firstname(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test"))
    app.kontact.modify_first_kontact(Kontact(firstname="Test_contact!!!"))



def test_modify_contact_middlename(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test"))
    app.kontact.modify_first_kontact(Kontact(middlename="Test_contact!!!"))

