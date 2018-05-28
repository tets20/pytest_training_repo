from model.kontact import Kontact
from random import randrange
import re



def test_all_user_info_on_homepage_by_index(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test",lastname="test"))
    kontacts = app.kontact.get_kontact_list()
    index = randrange(len(kontacts))
    print(index)
    kontact_from_homepage = app.kontact.get_kontact_list()[index]
    kontact_from_edit_page = app.kontact.get_kontact_info_from_edit_page(index)
    assert kontact_from_homepage.all_phones_from_homepage == merge_phones_like_on_home_page(kontact_from_edit_page)
    assert kontact_from_homepage.all_email_from_homepage == merge_email_like_on_home_page(kontact_from_edit_page)
    assert kontact_from_homepage.firstname == kontact_from_edit_page.firstname
    assert kontact_from_homepage.lastname == kontact_from_edit_page.lastname


def test_check_info_on_home_page_and_in_db(app,db):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test",lastname="test"))
    list_kontakts_on_homepage = app.kontact.get_kontact_list()
    list_kontakts_from_bd = db.get_kontact_list()

    for kontact in range(len(sorted(list_kontakts_on_homepage,key=Kontact.id_or_max))):
        kontact_home_page = sorted(list_kontakts_on_homepage,key=Kontact.id_or_max)[kontact]
        kontact_from_bd = sorted(list_kontakts_from_bd,key=Kontact.id_or_max)[kontact]

        assert kontact_home_page.all_email_from_homepage == merge_email_like_on_home_page(kontact_from_bd)
        assert kontact_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(kontact_from_bd)
        assert kontact_home_page.id == kontact_from_bd.id
        assert kontact_home_page.firstname == kontact_from_bd.firstname
        assert kontact_home_page.lastname == kontact_from_bd.lastname





def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(kontact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [kontact.home, kontact.mobile, kontact.work, kontact.phone2]))))

def merge_email_like_on_home_page(kontact):
    return "\n".join(filter(lambda x: x != "",filter(lambda x: x is not None,
                                                     [kontact.email, kontact.email2, kontact.email3])))

