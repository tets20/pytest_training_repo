# -*- coding: utf-8 -*-

from model.kontact import Kontact
import os.path
import random
import string
import getopt #для чтения опций командной строки
import jsonpickle
import sys # чтобы получить доступ к этим опциям


try:
    opts,args = getopt.getopt(sys.argv[1:],"n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/kontacts.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
]




file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(Testdata))
