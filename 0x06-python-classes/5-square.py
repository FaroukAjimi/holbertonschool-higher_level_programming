#!/usr/bin/python3
class Square:
    '''square funtion lvl 5'''
    def __init__(self, size=0):
        '''funtion square
        args
        size:0'''
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
        '''fucntion size
        args
        none
        return:size'''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''function size 2
        args :
        value: size'''
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
        '''funciton area
        args
        None
        return a'''
        a = self.__size * self.__size
        return(a)

    def my_print(self):
        '''function my_print
        args
        None
        print'''
        for i in range(self.__size):
            for y in range(self.__size):
                print('#', end="")
            print()
        if (self.__size == 0):
            print()
