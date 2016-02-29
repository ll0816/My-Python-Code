# !/usr/bin/python
# -*- coding: utf-8 -*-
# 1.10. Removing Duplicates from a Sequence while Maintaining Order
# Liu L.
# 02-28-16

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    print seen

a = [1, 5, 2, 1, 9, 1, 5, 18]
print list(dedupe(a))

def dedupe_2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
    print seen

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print list(dedupe_2(a, key=lambda d: (d['x'], d['y'])))