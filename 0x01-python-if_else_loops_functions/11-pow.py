#!/usr/bin/python3
def pow(a, b):
    c = 1
    if b < 0:
        b = b * -1
        c = float(c)
        a = float(a)
        for i in range(0, b):
            c = c / a
        return c
    if b >= 0:
        for i in range(b):
            c = c * a
        return c
