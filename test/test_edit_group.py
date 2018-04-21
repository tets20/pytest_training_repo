# -*- coding: utf-8 -*-

from model.group import Group



def test_edit_group(app):
    app.session.login( username="admin", password="secret")
    app.group.edit_first_group(Group(name="Test1", header="Test_group1", footer="Test_group1"))
    app.session.logout()


