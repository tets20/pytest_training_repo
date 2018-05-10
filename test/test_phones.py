from random import randrange
import re


def test_phones_on_homepage(app):
    kontact_from_homepage = app.kontact.get_kontact_list()[0]
    kontact_from_edit_page = app.kontact.get_kontact_info_from_edit_page(0)
    assert kontact_from_homepage.all_phones_from_homepage == merge_phones_like_on_home_page(kontact_from_edit_page)


def test_phones_on_kontact_view_page(app):
    kontact_from_view_page = app.kontact.get_kontact_from_view_page(0)
    kontact_from_edit_page = app.kontact.get_kontact_info_from_edit_page(0)
    assert kontact_from_view_page.home == kontact_from_edit_page.home
    assert kontact_from_view_page.mobile == kontact_from_edit_page.mobile
    assert kontact_from_view_page.work == kontact_from_edit_page.work
    assert kontact_from_view_page.phone2 == kontact_from_edit_page.phone2





def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(kontact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [kontact.home, kontact.mobile, kontact.work, kontact.phone2]))))

