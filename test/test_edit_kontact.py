# -*- coding: utf-8 -*-

from model.kontact import Kontact

def test_edit_contact(app):
    app.session.login( username="admin", password="secret")
    app.kontact.edit_first_kontact(Kontact(firstname="Test_contact1", middlename="Test_contact1",
                                           lastname="Test_contact1",nickname="TC1", title="Test_user1",
                                           company="Test_company1", address="Test_country1",
                               home="Home_test1", mobile="00-00-00", work="00-00-00", fax="00-00-00",
                               email="4test@test.ru", email2="5test@test.ru", email3="6test@test.ru",
                               homepage="test.test.ru", byear="1901", ayear="1991", address2="Test_city1",
                               home2="Test_home", notes="Test_contact1"))
    app.session.logout()
