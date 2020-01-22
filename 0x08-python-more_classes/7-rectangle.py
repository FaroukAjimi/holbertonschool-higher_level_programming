#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not(isinstance(value, int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')

    @property
    def height(self, width, height):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not(isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ('')
        width = '{}'.format(self.print_symbol) * self.__width
        rect = width
        for i in range(self.__height - 1):
            rect += '\n'
            rect += width
        return rect

    def __repr__(self):
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
