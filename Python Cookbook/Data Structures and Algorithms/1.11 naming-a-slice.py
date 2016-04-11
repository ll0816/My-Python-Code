# !/usr/bin/python
# -*- coding: utf-8 -*-
# 1.11. Naming a Slice
# Liu L.
# 03-04-2016

'''
In general, the built-in slice() creates a slice object that can be used anywhere a slice is allowed.
'''

record = '....................100          .......513.25     ..........'

cost = int(record[20:32]) * float(record[40:48])

# Alternative

SHARES = slice(20,32)
PRICE  = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print items
print 'items[2:4]:', items[2:4]
print 'items[a]:', items[a]
items[a] = [10, 11]
print 'items[a] = [10, 11]:', items
del items[a]
print 'del items[a]:', items
print '-' * 20

a = slice(10, 50, 2)
a.start
a.stop
a.step

s = 'HelloWorld'
a.indices(len(s))

