#!/usr/bin/python3
"""
Module that contains function
"""


def read_file(filename=""):
    """function read_file
       Args:
           filename
    """
    with open(filename, "r") as f:
        data = f.read()
        print (data, end='')
