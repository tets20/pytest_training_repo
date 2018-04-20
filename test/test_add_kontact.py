# -*- coding: utf-8 -*-

from model.kontact import Kontact

def test_add_contact(app):
    app.session.login( username="admin", password="secret")
    app.kontact.create(Kontact(firstname="Test_contact", middlename="Test_contact", lastname="Test_contact",
                               nickname="TC", title="Test_user", company="Test_company", address="Test_country",
                               home="Home_test", mobile="00-00-00", work="00-00-00", fax="00-00-00",
                               email="1test@test.ru", email2="2test@test.ru", email3="3test@test.ru",
                               homepage="test.test.ru", byear="1901", ayear="1991", address2="Test_city",
                               home2="Test_home", notes="Test_contact"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login( username="admin", password="secret")
    app.kontact.create(Kontact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                               homepage="", byear="", ayear="", address2="", home2="", notes=""))
    app.session.logout()


