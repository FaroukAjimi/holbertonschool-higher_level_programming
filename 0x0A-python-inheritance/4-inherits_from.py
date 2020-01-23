#!/usr/bin/python3
"""module that contains functions"""


def inherits_from(obj, a_class):
    """inherits_from function"""
    return isinstance(obj, a_class) and type(obj) is not a_class
