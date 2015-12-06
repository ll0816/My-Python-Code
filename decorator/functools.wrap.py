# !/usr/bin/python
# -*- coding: utf-8 -*-
# functools.wrap
# Liu L.
# 12-05-15

import datetime
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwagrs):
        print "Calling function: {} at {}".format(func.__name__, datetime.datetime.now())
        func(*args, **kwagrs)
        print "Finished calling: {}".format(func.__name__)
    return wrapper

@logger
def print_full_name(*args, **kwagrs):
    """return Liu L.'s full name"""
    print "My name is {} {}".format(*args)

if __name__ == '__main__':
    print print_full_name.__doc__
    print print_full_name.__name__