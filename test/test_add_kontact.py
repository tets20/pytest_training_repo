# -*- coding: utf-8 -*-

from model.kontact import Kontact
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation +" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


Testdata =[Kontact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                               homepage="", byear="", ayear="", address2="", phone2="", notes="")] + [
    Kontact(firstname=random_string("firstname",4), middlename=random_string("middlename",4),
            lastname=random_string("lastname",4),
            nickname=random_string("nickname", 5),title=random_string("title",5),company=random_string("company",5),
            address=random_string("address",3),home=random_string("home",3),mobile=random_string("mobile",3),
            work=random_string("work",2),fax=random_string("fax",5), email=random_string("email",5),
            email2=random_string("email2",3),
            email3=random_string("email3",4), homepage=random_string("homepage",5),byear=random_string("byear",6),
            ayear=random_string("ayear",3), address2=random_string("address2",5), phone2=random_string("phone2",5),
            notes=random_string("notes",20))
    for i in range(5)
]

@pytest.mark.parametrize("kontact",Testdata, ids = [repr(x) for x in Testdata])
def test_add_kontact(app,kontact):
    old_kontacts = app.kontact.get_kontact_list()
    app.kontact.create(kontact)
    assert len(old_kontacts) + 1 == app.kontact.count()
    new_kontacts = app.kontact.get_kontact_list()
    old_kontacts.append(kontact)
    assert sorted(old_kontacts, key = Kontact.id_or_max) == sorted(new_kontacts, key = Kontact.id_or_max)




