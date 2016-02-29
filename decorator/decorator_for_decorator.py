# !/usr/bin/python
# -*- coding: utf-8 -*-
# decorator for decorator
# Liu L.
# 12-05-12
# Source: https://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python?answertab=oldest#tab-top

def decorator_with_args(decorator_to_enhance):
    """
    This function is supposed to be used as a decorator.
    It must decorate an other function, that is intended to be used as a decorator.
    Take a cup of coffee.
    It will allow any decorator to accept an arbitrary number of arguments,
    saving you the headache to remember how to do that every time.
    """

    # We use the same trick we did to pass arguments
    def decorator_maker(*args, **kwargs):

        # We create on the fly a decorator that accepts only a function
        # but keeps the passed arguments from the maker.
        def decorator_wrapper(func):

            # We return the result of the original decorator, which, after all,
            # IS JUST AN ORDINARY FUNCTION (which returns a function).
            # Only pitfall: the decorator must have this specific signature or it won't work:
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker

# You create the function you will use as a decorator. And stick a decorator on it :-)
# Don't forget, the signature is "decorator(func, *args, **kwargs)"
@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(*function_args):
        print " ".join(args), kwargs.values()
        return func(*function_args)
    return wrapper

# Then you decorate the functions you wish with your brand new decorated decorator.

@decorated_decorator("This", "is", "a decorated decorator", say = "Yeeeep!")
def decorated_function(*function_args):
    print "Hello, {} {}".format(*function_args)

if __name__ == '__main__':
    decorated_function("Python and", "Java!")
