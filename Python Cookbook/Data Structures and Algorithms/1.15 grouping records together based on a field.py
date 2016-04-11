# !/usr/bin/python
# -*- coding: utf-8 -*-
# 1.15. Grouping Records Together Based on a Field
# Liu L.
# 11/04/2016

print "1.15. Grouping Records Together Based on a Field"
print "You have a sequence of dictionaries or instances and you want to iterate over the data in groups based on the value of a particular field, such as date."

from operator import itemgetter
from itertools import groupby

rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}]

# Sort by the desired field first
rows.sort(key = itemgetter('date'))

# Iterate in groups
for date, items in groupby(rows, key = itemgetter('date')):
    print date
    for i in items:
        print '     ', i
