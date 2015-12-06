# !/usr/bin/python
# -*- coding: utf-8 -*-
# dive in decorator
# Liu L.
# 12-05-15

def decorator_maker():
    print "I make decorators! I am executed only once:"+\
    "when you make me create a decorator"

    def my_decorator(func):
        print "I am a decorator! I am executed"+\
         "only when you decorate a function."

        def wrapper():
            print "I am the wrapper around the decorated function. "+\
                  "I am called when you call the decorated function. "+\
                  "As the wrapper, I return the RESULT of the decorated function."
            return func()

        print "As the decorator, I return the wrapped function."
        return wrapper
    print "As a decorator maker, I return a decorator"
    return my_decorator

if __name__ == '__main__':
    def decorated_func():
        print "I am the decorated function"

    decorated_function = decorator_maker()(decorated_func)
    decorated_function()

    print "\n"

    @decorator_maker()
    def decorated_func2():
        print "I am the decorated function."
    decorated_func2()