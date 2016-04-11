# !/usr/bin/python
# -*- coding: utf-8 -*-
# 1.3 Keeping the Last N Items
# Liu L.
# 01-05-2016

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# q.appendleft(4)
# q.pop()
# q.popleft()