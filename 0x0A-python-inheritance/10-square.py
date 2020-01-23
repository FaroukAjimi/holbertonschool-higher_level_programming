#!/usr/bin/python3
"""module that contains class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """"init function"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """area function"""
        return (self.__size ** 2)
