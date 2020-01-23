#!/usr/bin/python3
""" Module That contains function"""


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class function"""
    if isinstance(obj, a_class) is True:
        return(True)
    else:
        return(False)
