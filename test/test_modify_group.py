# -*- coding: utf-8 -*-

from model.group import Group
import random
from random import randrange



def test_modify_group_name(app,db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_mod = Group(name="New_group")
    app.group.modify_group_by_id(group.id, group_mod)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_modify_group_header(app,db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_mod = Group(header="New_header")
    app.group.modify_group_by_id(group.id, group_mod)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)