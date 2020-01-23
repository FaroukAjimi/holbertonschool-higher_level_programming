#!/usr/bin/python3
""" this module contains a function"""


def add_attribute(cls, name, value):
    """add atribute function"""
    try:
        setattr(cls, name, value)
    except:
        raise TypeError("can't add new attribute")
