# !/usr/bin/python
# -*- coding: utf-8 -*-
# general decorator
# Liu L.
# 12-05-15

def decorator(func):
    def wrapper(*args, **kwargs):
        print args
        print kwargs
        func(*args, **kwargs)
    return wrapper

@decorator
def func_with_no_arg():
    print "Cool"

@decorator
def func_with_args(a, b, c):
    print a, b, c

@decorator
def func_with_named_args(a, b, c, language = "Why not?"):
    print "Do %s, %s and %s like language? %s" %\
    (a, b, c, language)

if __name__ == '__main__':
    print func_with_no_arg(), '\n'
    print func_with_args(1, 2, 3), '\n'
    print func_with_named_args("Python", "Ruby", "Java", language="Indeed!")