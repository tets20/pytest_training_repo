# -*- coding: utf-8 -*-
from sys import maxsize

class Kontact:
    def __init__(self, firstname = None, middlename= None, lastname= None, nickname= None, title= None, company= None,
                 address= None, home= None, mobile= None, work= None, fax= None, email= None, email2= None,
                 email3= None, homepage= None, byear= None, ayear= None, address2= None, phone2= None, notes= None,
                 id = None, all_phones_from_homepage=None, all_email_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_email_from_homepage = all_email_from_homepage

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.middlename,self.all_phones_from_homepage)


    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id , self.firstname == other.firstname ,\
               self.lastname == other.lastname, self.middlename == other.middlename



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
