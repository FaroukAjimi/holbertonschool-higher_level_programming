#!/usr/bin/python3
"""Module that contains class"""


class BaseGeometry:
    """a class that contains 2 fucntions"""

    def area(self):
        """area function"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_calidation function"""
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
        pass
