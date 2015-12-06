# !/usr/bin/python
# -*- coding: utf-8 -*-
# defining func with * and **
# Liu L.
# 12-05-15

def show_args(arg, *args, **kwargs):
    print arg
    for item in args:
        print item
    for key, value in kwargs:
        print key, value

if __name__ == '__main__':
    args = [1, 2, 3, 4]
    show_args("hey", *args)