# !/usr/bin/python
# -*- coding: utf-8 -*-
# 1.6 Mapping Keys to Multiple Values in a Dictionary
# Liu L.
# 02-210=-2016

from collections import defaultdict

d = defaultdict(list)
print d
print '-'*20

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print d
print '-'*20

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(1)
d['b'].add(1)
print d
print '-'*20

d = {}
d.setdefault('a', []).append(1)
print d
d.setdefault('a', []).append(2)
print d
d.setdefault('b', []).append(4)
print d


print '''
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
'''