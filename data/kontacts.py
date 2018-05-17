# -*- coding: utf-8 -*-

from model.kontact import Kontact


Testdata =[Kontact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
                   title="title1", company="company1",
                               address="address1", home="home1", mobile="mobile1", work="work1", fax="fax1",
                   email="email1", email2="email21", email3="email31",
                               homepage="homepage1", byear="byear1", ayear="ayear1", address2="address21",
                   phone2="phone21", notes="notes1"),
            Kontact(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2",
                    title="title2", company="company2",
                                   address="address2", home="home2", mobile="mobile2", work="work2", fax="fax2",
                    email="email2", email2="email22", email3="email32",
                                   homepage="homepage2", byear="byear2", ayear="ayear2", address2="address22",
                    phone2="phone22", notes="notes2")
           ]