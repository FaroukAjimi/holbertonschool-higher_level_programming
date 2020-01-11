#!/usr/bin/python3
class Square:
    '''Square functin level 2'''
    def __init__(self, size=0):
        '''square fuction
        Args:
        size: 0
        '''
        self.__size = size
        try:
            if(isinstance(size, int) == False):
                raise TypeError
            if (size < 0):
                raise ValueError
        except TypeError as e:
            raise Exception('size must be an integer')
        except ValueError as e:
            raise Exception('size must be >= 0')
