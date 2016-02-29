# !/usr/bin/python
# -*- coding: utf-8 -*-
# 1.7 Keeping Dictionaries in Order
# Liu L.
# 02-21-2016

'''
Notice the size of an OrderedDict is more than twice
as large as a normal dictionary due to the
extra linked list that’s created.
'''
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print key, d[key]
print '-' * 20

import json
print json.dumps(d)