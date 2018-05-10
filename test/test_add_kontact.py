# -*- coding: utf-8 -*-

from model.kontact import Kontact

def test_add_kontact(app):
    old_kontacts = app.kontact.get_kontact_list()
    kontact = Kontact(firstname="Test_contact", middlename="Test_contact", lastname="Test_contact",
                               nickname="TC", title="Test_user", company="Test_company", address="Test_country",
                               home="Home_test", mobile="334 1", work="123-", fax="3()",
                               email="1test@test.ru", email2="2test@test.ru", email3="3test@test.ru",
                               homepage="test.test.ru", byear="1901", ayear="1991", address2="Test_city",
                               phone2="Test_home", notes="Test_contact")
    app.kontact.create(kontact)
    assert len(old_kontacts) + 1 == app.kontact.count()
    new_kontacts = app.kontact.get_kontact_list()
    old_kontacts.append(kontact)
    assert sorted(old_kontacts, key = Kontact.id_or_max) == sorted(new_kontacts, key = Kontact.id_or_max)




'''def test_add_empty_kontact(app):
    old_kontacts = app.kontact.get_kontact_list()
    kontact = Kontact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                               homepage="", byear="", ayear="", address2="", phone2="", notes="")
    app.kontact.create(kontact)
    assert len(old_kontacts) + 1 == app.kontact.count()
    new_kontacts = app.kontact.get_kontact_list()
    old_kontacts.append(kontact)
    assert sorted(old_kontacts, key = Kontact.id_or_max) == sorted(new_kontacts, key = Kontact.id_or_max)'''


