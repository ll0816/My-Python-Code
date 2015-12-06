# !/usr/bin/python
# -*- coding: utf-8 -*-
# generator expression
# Liu L.
# 12-05-15

squares = (i**2 for i in range(10))
squares
for square in squares:
    print square