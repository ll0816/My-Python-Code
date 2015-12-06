# !/usr/bin/python
# -*- coding: utf-8 -*-
# decorator maker with arguments
# Liu L.
# 12-05-15

def decorator_maker_with_args(d_arg1, d_arg2):
    print "I make decorators! And I accept arguments:{} {}".format(d_arg1, d_arg2)

    def decorator(func):
        print "I am the decorator. Somehow you passed me arguments: {} {}".format(d_arg1, d_arg2)

        def wrapper(*args):
            print ("I am the wrapper around the decorated function.\n"
                  "I can access all the variables\n"
                  "\t- from the decorator: {0} {1}\n"
                  "\t- from the function call: {2} {3}\n"
                  "Then I can pass them to the decorated function"
                  .format(d_arg1, d_arg2, *args))
            return func(*args)
        return wrapper
    return decorator

@decorator_maker_with_args("Leonard", "Sheldon")
def decorated_func_with_args(*args):
    print ("I am the decorated function and only knows about my arguments: {0}"
           " {1}".format(*args))
if __name__ == '__main__':
    decorated_func_with_args("Rajesh", "Howard")