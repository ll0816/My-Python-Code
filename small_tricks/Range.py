# !/usr/bin/python
# -*- coding: utf-8 -*-
# self defined range iterator
# Liu L.
# 12-05-15

class Range:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.curr = 0
        return self

    def next(self):
        numb = self.curr
        if self.curr >= self.max:
            raise StopIteration
        self.curr += 1
        return numb

if __name__ == '__main__':
    print [i for i in Range(10)]