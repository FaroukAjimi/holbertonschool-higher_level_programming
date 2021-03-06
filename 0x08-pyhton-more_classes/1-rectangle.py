#!/usr/bin/python3
"""module rectangle"""


class Rectangle:
    """class rectangle
    args: width
    height"""

    def __init__(self, width=0, height=0):
        """fucntion
        args
        width
        height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """function width
        arg:self"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        args: self
        value"""
        self.__width = value
        if not(isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')

    @property
    def height(self):
        """funciton height
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
