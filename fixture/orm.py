from datetime import datetime
from pony.orm import *
from model.group import Group
from model.kontact import Kontact
from pymysql.converters import decoders


class ORMFixture:

    db=Database()

    class ORMGroup(db.Entity):

        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str,column='group_footer')

    class ORMKontact(db.Entity):

        _table_ = "addressbook"
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column="deprecated")#для групп - datetime поставить


    def convert_to_groups_from_modal(self,groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name,header=group.header,footer=group.footer)

        return list(map(convert, groups))


    def convert_to_kontacts_from_modal(self,kontacts):
        def convert(kontact):
            return Kontact(id=str(kontact.id), firstname=kontact.firstname, lastname=kontact.lastname)
        return list(map(convert, kontacts))


    def __init__(self,host,name,user,password):
        self.db.bind('mysql',host=host, database = name, user =user, password =password,conv =decoders)#привязка к дб
        self.db.generate_mapping()
        sql_debug(True)


    @db_session
    def get_group_list(self):
        return self.convert_to_groups_from_modal(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_kontact_list(self):
        return self.convert_to_kontacts_from_modal(select(c for c in ORMFixture.ORMKontact if c.deprecated is None))