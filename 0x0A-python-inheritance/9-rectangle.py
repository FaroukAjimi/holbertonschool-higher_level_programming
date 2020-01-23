#!/usr/bin/python3
"""Module that contains a class"""


Rectangle = __import__('8-rectangle').Rectangle


class Rectangle(Rectangle):
    """rectangle class"""

    def __init__(self, width, height):
        """init function"""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """area function"""
        return(self.__width * self.__height)

    def __str__(self):
        """str function"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
