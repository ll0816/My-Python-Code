# !/usr/bin/python
# -*- coding: utf-8 -*-
# Decorating methods
# Liu L.
# 12-05-15

def method_decorator(method):
    def wrapper(self, lie):
        lie -= 3
        return method(self, lie)
    return wrapper

class Lucy(object):
        def __init__(self):
            self.age = 32

        @method_decorator
        def sayYourAge(self, lie):
            print "I am %s, what did you think?" %(self.age + lie)

if __name__ == '__main__':
    l = Lucy()
    l.sayYourAge(-3)