# -*- coding: utf-8 -*-


from data.groups import constant as Testdata
from model.group import Group
import pytest



@pytest.mark.parametrize("group",Testdata, ids = [repr(x) for x in Testdata])
def test_add_group(app,group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


