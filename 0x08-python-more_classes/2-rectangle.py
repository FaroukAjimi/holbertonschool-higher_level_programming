#!/usr/bin/python3
"""module rectangle"""


class Rectangle:
    """class rectangle
    args: width
    height"""

    def __init__(self, width=0, height=0):
        """init funciton
        height
        width"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """function width
        args
        self"""
        return self.__width

    @width.setter
    def width(self, value):
        """funciton width
        args
        self
        value"""
        self.__width = value
        if not(isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')

    @property
    def height(self):
        """function height
        args
        self"""
        return self.__height

    @height.setter
    def height(self, value):
        """function height
        args
        self
        value"""
        self.__height = value
        if not(isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')

    def area(self):
        """fucntion area
        args
        self"""
        return (self.__width * self.__height)

    def perimeter(self):
        """function perimeter
        args
        self"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (self.__width * 2 + self.__height * 2)
