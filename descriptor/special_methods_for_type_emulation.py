# !/usr/bin/python
# -*- coding: utf-8 -*-
# special methods for Type Emulation
# Liu L.
# 12-05-15
# source: http://intermediatepythonista.com/classes-and-objects

class CustomList(object):
    def __init__(self, container = None):
        if container is None:
            self.container = []
        else:
            self.container = container

    def __len__(self):
        return len(self.container)

    def __getitem__(self, index):
        return self.container[index]

    def __setitem__(self, index, value):
        if index <= len(self.container):
            self.container[index] = value
        else:
            raise IndexError()

    def __contains__(self, value):
        return value in self.container

    def append(self, value):
        self.container.append(value)

    def __repr__(self):
        return str(self.container)

    def __add__(self, otherList):
        return CustomList(self.container + otherList.container)

if __name__ == '__main__':
    myList = CustomList()
    myList.append(1)
    myList.append(2)
    myList.append(3)
    myList.append(4)
    print len(myList)
    print 4 in myList