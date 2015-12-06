# !/usr/bin/python
# -*- coding: utf-8 -*-
# looger
# Liu L.
# 12-05-15

import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling function: {} at {}".format(func.__name__, datetime.datetime.now()))
        func(*args, **kwargs)
        print("Finished calling: {}".format(func.__name__))
    return wrapper

@logger
def print_full_name(first, last):
    print("My name is {} {}".format(first, last))

if __name__ == '__main__':
    print_full_name("Liu", "L.")