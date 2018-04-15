# -*- coding: utf-8 -*-
from application import Application
from group import Group
import pytest



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login( username="admin", password="secret")
    app.create_group(Group(name="Test", header="Test_group", footer="Test_group"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

