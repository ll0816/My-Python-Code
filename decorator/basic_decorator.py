# !/usr/bin/python
# -*- coding: utf-8 -*-
# basic decorator
# Liu L.
# 12-05-15

def bread(func):
    def wrapper():
        print "</''''''\>"
        func()
        print "<\''''''/>"
    return wrapper

def ingredients(func):
    def wrapper():
        print "#tomatoes#"
        func()
        print "~salad~"
    return wrapper

@bread
@ingredients
def sandwich(food="--ham--"):
    print food

if __name__ == '__main__':
    sandwich()