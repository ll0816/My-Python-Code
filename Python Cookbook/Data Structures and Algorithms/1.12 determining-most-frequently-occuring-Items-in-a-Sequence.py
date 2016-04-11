# !/usr/bin/python
# -*- coding: utf-8 -*-
# 1.12 Determining the Most Frequently Occuring Items in a Sequence
# Liu L.
# 03/18/201

words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print top_three
print '-'*20

word_counts['not']
word_counts['eyes']

morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)
a = Counter(words)
b = Counter(morewords)
c = a + b
print c
print '-'*20

d = a - b
print d