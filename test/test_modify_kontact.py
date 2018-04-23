# -*- coding: utf-8 -*-

from model.kontact import Kontact

def test_modify_contact_firstname(app):
    app.session.login( username="admin", password="secret")
    app.kontact.modify_first_kontact(Kontact(firstname="Test_contact!!!"))
    app.session.logout()


def test_modify_contact_middlename(app):
    app.session.login( username="admin", password="secret")
    app.kontact.modify_first_kontact(Kontact(middlename="Test_contact!!!"))
    app.session.logout()
