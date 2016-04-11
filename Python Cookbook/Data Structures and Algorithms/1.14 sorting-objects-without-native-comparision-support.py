# !/usr/bin/python
# -*- coding: utf-8 -*-
# 1.14 Sorting Objects Without Native Comparision Support
# Liu L.
# 03-18-2016

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(99), User(3), User(23)]
print sorted(users, key=lambda u: u.user_id)
print '-'*20
# Or use operator.attrgetter():
from operator import attrgetter
print sorted(users, key=attrgetter('user_id'))

# by_name = sorted(users, key=attrgetter('last_name', 'first_name'))