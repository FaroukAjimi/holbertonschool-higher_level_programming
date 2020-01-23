#!/usr/bin/python3
"""Module that contains class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        """init function"""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
