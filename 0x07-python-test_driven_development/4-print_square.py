#!/usr/bin/python3
"""This module
is to print a square
based on the given size
size must be an integer
otherwise an Error will occur"""


def print_square(size):
    """function print_square
    args:
    size"""
    if not(isinstance(size, int)):
        raise TypeError('size must be an integer')
    elif isinstance(size, float) and (size < 0):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for y in range(size):
            print('#', end='')
        print()
