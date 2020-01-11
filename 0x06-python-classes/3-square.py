#!/usr/bin/python3
class Square:
    '''square fuction lvl 3'''
    def __init__(self, size=0):
        '''function 3
        Args
        size:'''
        self.__size = size
        try:
            size += 1
            if(size < 0):
                raise(ValueError)
        except TypeError:
            raise Exception('size must be an integer')
        except ValueError:
            raise Exception('size must be >= 0')

    def area(self):
            '''area function
            Args
            return: a'''
            a = self.__size * self.__size
            return(a)
