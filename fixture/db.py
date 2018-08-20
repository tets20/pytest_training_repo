import pymysql.cursors
from model.group import Group
from model.kontact import Kontact


class DbFixture:
    def __init__(self,host,name,user,password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database = name, user =user, password =password)
        self.connection.autocommit(True) # отрубаем кэш



    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id,group_name, group_header, group_footer from group_list" )
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Group(id=str(id),name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list


    def get_kontact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, email, email2, email3, home ,mobile ,work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id,firstname,lastname, email, email2, email3, home ,mobile ,work,phone2) = row
                list.append(Kontact(id=str(id), firstname=firstname, lastname=lastname,
                                    email=email,email2=email2,email3=email3,home=home,mobile=mobile,work=work,phone2=phone2))
        finally:
            cursor.close()
        return list



    def destroy(self):
        self.connection.close()