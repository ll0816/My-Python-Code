# !/usr/bin/python
# -*- coding: utf-8 -*-
# Decorator function with Function Args
# Liu L.
# 12-05-15

import datetime

def decorator_maker_with_args(decorator_arg1):
    def decorator(func):
        def wrapper(*args):
            print "Calling function: {} at {} with decorator arguments: {} and function arguments {}".\
            format(func.__name__, datetime.datetime.now(), decorator_arg1, args)
            func(*args)
            print "Finished calling: {}".format(func.__name__)
        return wrapper
    return decorator

@decorator_maker_with_args("Apollo 11 Landing")
def print_name(*args):
    print "My full name is -- {} {} --".format(*args)

if __name__ == '__main__':
    print_name("Tranquility base", "To Houston")

    def print_age(*args):
        print "My age is -- {} --".format(*args)
    decorated_func = decorator_maker_with_args("Boston")(print_age)
    decorated_func(23)