#!/usr/bin/python3
class Square:
    '''function square lvl 4'''
    def __init__(self, size=0):
        '''function
        args
        size: 0'''
        self.__size = size
        try:
            size += 1
            if(size < 0):
                raise(ValueError)
        except TypeError:
            raise Exception('size must be an integer')
        except ValueError:
            raise Exception('size must be >= 0')

    @property
    def size(self):
        '''function size
        args
        size:0
        return:size'''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''function size2
        args
        size:value'''
        try:
            isinstance(value, int)
            if(value < 0):
                raise(ValueError)
        except TypeError:
            raise Exception('size must be an integer')
        except ValueError:
            raise Exception('size must be >= 0')
        self.__size = value

    def area(self):
        '''function area
        args
        none
        return: a'''
        a = self.__size * self.__size
        return(a)
