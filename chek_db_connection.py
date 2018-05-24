import pymysql.cursors
from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name = "addressbook", user ="root", password ="")

try:
    kontacts= db.get_kontact_list()
    for kontakt in kontacts:
        print(kontakt)
        print(len(kontacts))
finally:
    db.destroy()