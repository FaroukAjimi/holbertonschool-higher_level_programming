#!/usr/bin/python3
class Square:
    '''square funtion'''
    def __init__(self, size=0, position=(0, 0)):
        '''fnction squarr
        args
        size: 0
        position 0,0'''
        self.__size = size
        self.__position = position
        try:
            size += 1
            if(size < 0):
                raise(ValueError)
        except TypeError:
            raise Exception('size must be an integer')
        except ValueError:
            raise Exception('size must be >= 0')

    @property
    def position(self):
        '''fucntion position
        args
        None
        return None'''
        return(self.__position)

    @position.setter
    def position(self, value):
        '''function position
        args
        value:'''
        self.__position = value
        try:
            isinstance(value[0], int)
            isinstance(value[1], int)
            if(len(value) != 2) or (value[0] < 0) or (value[1] < 0):
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        '''funtion size
        args
        None
        return size'''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''functions
        args
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
        '''function area
        args
        None
        return a'''
        a = self.__size * self.__size
        return(a)

    def my_print(self):
        '''function my print
        args
        None
        print'''
        try:
            if (len(self.__position)) != 2:
                raise TypeError
            if (self.__position[0] < 0 or self.__position[1] < 0):
                raise TypeError
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for z in range(self.__position[0]):
                    print(" ", end="")
                for s in range(self.__size):
                    print('#', end="")
                print()
            if (self.__size == 0):
                print()
        except TypeError:
            print("position must be a tuple of 2 positive integers")
