# !/usr/bin/python
# -*- coding: utf-8 -*-
# Iterator for Fibonacci
# Liu L.
# 12-05-2015

class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def next(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == '__main__':
    print [i for i in Fib(10)]