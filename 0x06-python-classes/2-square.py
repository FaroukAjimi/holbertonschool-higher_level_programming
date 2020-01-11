#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
        try:
            size += 1
            if (size < 0):
                raise ValueError
        except TypeError as e:
            raise Exception('size must be an integer')
        except ValueError as e:
            raise Exception('size must be >= 0')
