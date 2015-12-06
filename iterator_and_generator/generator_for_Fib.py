# !/usr/bin/python
# -*- coding: utf-8 -*-
# Generator for Fibonacci
# Liu L.
# 12-05-15

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

if __name__ == '__main__':

    gen = fib(10)
    while True:
        try:
            print next(gen)
        except: break
