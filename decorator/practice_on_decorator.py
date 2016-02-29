# !/usr/bin/python
# -*- coding: utf-8 -*-
# practice on decorator
# Liu L.
# 12-05-15
# source: https://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python?answertab=oldest#tab-top

def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))
if __name__ == '__main__':
    print reverse_string("Able was I ere I saw Elba")
    print reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!")
    print "\n"

    @counter
    @benchmark
    @logging
    def get_random_futurama_quote():
        from urllib import urlopen
        result = urlopen("http://subfusion.net/cgi-bin/quote.pl?quote=futurama").read()
        try:
            value = result.split("<br><b><hr><br>")[1].split("<br><br><hr>")[0]
            return value.strip()
        except:
            return "No, I'm ... doesn't!"
    print get_random_futurama_quote()
    print get_random_futurama_quote()