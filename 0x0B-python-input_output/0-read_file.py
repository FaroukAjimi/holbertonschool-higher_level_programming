#!/usr/bin/python3
"""Module that contains function"""


def read_file(filename=""):
    """function readfile"""
    with open(filename) as file:
        data = file.read()
        print (data, end='')
