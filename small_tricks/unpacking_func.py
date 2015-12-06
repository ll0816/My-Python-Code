# !/usr/bin/python
# -*- coding: utf-8 -*-
# unpacking function
# Liu L.
# 12-05-15

def print_args(a, b):
    print a
    print b

def parrot(voltage, state='a stiff', action='voom'):
           print "-- This parrot wouldn’t", action,
           print "if you put", voltage, "volts through it.",
           print "E’s", state, "!"


if __name__ == '__main__':
    args = [1, 2]
    print_args(*args)

    d = {"voltage": "four million", "state": "bleedin’ demised", "action": "VOOM"}
    parrot(**d)