from datetime import datetime
from pony.orm import *
from model.group import Group
from model.kontact import Kontact
#from pymysql.converters import decoders
from pymysql.converters import encoders, decoders, convert_mysql_timestamp


class ORMFixture:

    db=Database()

    class ORMGroup(db.Entity):

        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str,column='group_footer')
        kontacts = Set(lambda: ORMFixture.ORMKontact,table='address_in_groups',column='id',reverse='groups',lazy=True)

    class ORMKontact(db.Entity):

        _table_ = "addressbook"
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column="deprecated")#для групп - datetime поставить
        groups = Set(lambda: ORMFixture.ORMGroup,table='address_in_groups',column='group_id',reverse='kontacts',lazy=True)

    def convert_to_groups_from_modal(self,groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name,header=group.header,footer=group.footer)

        return list(map(convert, groups))


    def convert_to_kontacts_from_modal(self,kontacts):
        def convert(kontact):
            return Kontact(id=str(kontact.id), firstname=kontact.firstname, lastname=kontact.lastname)
        return list(map(convert, kontacts))


    def __init__(self,host,name,user,password):

        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        #self.db.bind('mysql',host=host, database = name, user =user, password =password,conv =decoders)#привязка к дб
        self.db.generate_mapping()
        sql_debug(True)


    @db_session
    def get_group_list(self):
        return self.convert_to_groups_from_modal(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_kontact_list(self):
        return self.convert_to_kontacts_from_modal(select(c for c in ORMFixture.ORMKontact if c.deprecated is None))

    @db_session
    def get_kontacts_in_group(self,group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id==group.id))[0]
        return self.convert_to_kontacts_from_modal(orm_group.kontacts)

    @db_session
    def get_kontacts_not_in_group(self,group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id==group.id))[0]

        return self.convert_to_kontacts_from_modal(
            select(c for c in ORMFixture.ORMKontact if c.deprecated is None and orm_group not in c.groups))
