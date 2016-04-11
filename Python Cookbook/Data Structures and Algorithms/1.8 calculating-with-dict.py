# !/usr/bin/python
# -*- coding: utf-8 -*-
# 1.8 Calculating with Dictionaries
# Liu L.
# 02-22-2016

'''
zip() creates an iterator that can only be consumed once.
'''

prices = {
    'ACME' : 45.23,
    'AAPL' : 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20,
    'FB' : 10.75
}
print prices
print '-'*20

min_price = min(zip(prices.values(), prices.keys()))
print min_price
print '-'*20

max_price = max(zip(prices.values(), prices.keys()))
print max_price
print '-'*20

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print prices_sorted
print '-'*20

print 'To get the key corresponding to the min or max value'
print 'minimum value stock'
print min(prices, key = lambda k: prices[k])
print 'maximum value stock'
print max(prices, key = lambda k: prices[k])
print '-'*20

min_value = prices[min(prices, key = lambda k: prices[k])]
print min_value