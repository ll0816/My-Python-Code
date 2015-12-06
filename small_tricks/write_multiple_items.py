# !/usr/bin/python
# -*- coding: utf-8 -*-
# write multiple items
# Liu L.
# 12-05-15

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

if __name__ == '__main__':

    f = open("text.txt", 'w')
    write_multiple_items(f, " ", "one", "two", "three", "four", "five")